from django.db import models
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
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Please provide some brief information about where you made the recording - e.g. a suburb in Kyiv, etc.<br>Надайте коротку інформацію про те, де ви зробили запис, напр. передмістя в м. Києві тощо",
        verbose_name='location / Локація'
    )
    recording_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="date of recording / Дата запису",
        help_text="Please provide the date that the sound recording was produced"
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
    admin_approved = models.BooleanField(default=False, help_text="Sound data might be shared on the public website in the future. Please tick this box if you're happy for this sound to be included on the public website, if this feature is added in the future.")
    admin_notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sound #{self.id}: created {self.created}"
