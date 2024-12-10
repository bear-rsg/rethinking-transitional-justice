from django.db import models
from datetime import timedelta, datetime
import logging

logger = logging.getLogger(__name__)


class SoundUploadCode(models.Model):
    """
    A unique, random 6 digit code that is given to a single user to upload a sound
    Only users with a code can upload sounds
    """

    code = models.CharField(max_length=255, unique=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True, help_text="Input identifying information about which user this code has been assigned to (e.g. name, email)")
    admin_notes = models.TextField(blank=True, null=True)

    @property
    def sounds_count(self):
        return self.sounds.count()

    def __str__(self):
        return f'#{self.id} - {self.code}'


class Sound(models.Model):
    """
    A Sound that a member of public shares with the project
    """

    sound_upload_code = models.ForeignKey(SoundUploadCode, related_name='sounds', on_delete=models.PROTECT, blank=True, null=True)
    sound = models.FileField(
        upload_to='researchdata/sounds/',
        help_text="Please upload your sound recording here<br>Будь ласка завантажте Ваш звукозапис сюди",
        verbose_name='Sound / Звук'
    )
    photo = models.ImageField(
        upload_to='researchdata/photos/',
        blank=True,
        null=True,
        help_text="Please upload a photo related to this sound, to be shown on the public soundscape exhibition"
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Please provide some brief information about where you made the recording - e.g. a suburb in Kyiv, etc.<br>Надайте коротку інформацію про те, де ви зробили запис, напр. передмістя в м. Києві тощо",
        verbose_name='location / Локація'
    )

    location_soundscape_exhibition = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Location shown publicly in the soundscape exhibition'
    )
    location_soundscape_exhibition_ukrainian = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Location shown publicly in the soundscape exhibition (Ukrainian translation)'
    )

    recording_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="date of recording / Дата запису",
        help_text="Please provide the date that the sound recording was produced<br>Будь ласка, вкажіть дату створення звукозапису."
    )
    recording_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name="time of recording / Час запису",
        help_text="Please provide the time that the sound recording was produced (approximate hour, if exact time not known)<br>Будь ласка, вкажіть час, коли було створено звукозапис (приблизну годину доби, якщо точний час невідомий)"
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Please provide any important information about the recording - e.g. the main sounds that it captures, your feelings about the recording, etc.<br> Будь ласка, надайте будь-яку інформацію про запис – напр. основні звуки, які він вловлює, ваші почуття щодо запису тощо.",
        verbose_name='description / Опис'
    )
    description_ukrainian = models.TextField(blank=True, null=True, verbose_name='Description (Ukrainian translation)')

    interviewee_reflection = models.TextField(
        blank=True,
        null=True,
        help_text="Following an interview with author of this sound, include interesting reflections they've had about their submission"
    )
    interviewee_reflection_ukrainian = models.TextField(blank=True, null=True, verbose_name='Interviewee reflection (Ukrainian translation)')

    prompt_for_public_comments = models.TextField(blank=True, null=True, help_text="Provide a prompt (i.e. a question or statement) to encourage users to comment on this in the public website")

    related_sounds = models.ManyToManyField("self", blank=True, through='SoundsRelationship')
    order_in_soundscape_exhibition = models.FloatField(
        default=0,
        help_text="Sounds will be shown in the public soundscape exhibition in order of this value from lowest to highest"
    )
    admin_approved = models.BooleanField(default=False, help_text="Please tick this box if you're happy for this sound to be included in the public sound exhibition.")
    admin_notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def author(self):
        if self.sound_upload_code and self.sound_upload_code.assigned_to:
            return self.sound_upload_code.assigned_to

    @property
    def description_preview(self):
        return f'{self.description[:50]}...' if len(self.description) > 50 else self.description

    def __str__(self):
        return f"Sound #{self.id}: created {str(self.created)[:16]}"

    def save(self, *args, **kwargs):
        # Prevent users from submitting duplicate sounds by
        # ignoring saves of matching records within the last 10 seconds
        ten_seconds_ago = datetime.now() - timedelta(seconds=10)
        if not Sound.objects.filter(
            sound_upload_code=self.sound_upload_code,
            location=self.location,
            description=self.description,
            created__gte=ten_seconds_ago
        ):
            super().save(*args, **kwargs)


class SoundsRelationship(models.Model):
    """
    A relationship between 2 Sound objects, including details about their relationship
    """

    sound_1 = models.ForeignKey(Sound, related_name='sound_relationship_1', on_delete=models.RESTRICT)
    sound_2 = models.ForeignKey(Sound, related_name='sound_relationship_2', on_delete=models.RESTRICT)
    relationship_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Relationship between Sound #{self.sound_1.id} and Sound #{self.sound_2.id}"


class SoundscapeExhibitionComment(models.Model):
    """
    A comment made about a Sound in the soundscape exhibition
    """

    sound = models.ForeignKey(Sound, related_name='soundscape_exhibition_comment', on_delete=models.RESTRICT)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    admin_approved = models.BooleanField(default=False, help_text="Sound data might be shared on the public website in the future. Please tick this box if you're happy for this sound to be included on the public website, if this feature is added in the future.")

    def __str__(self):
        return f"A comment about Sound #{self.sound.id}"
