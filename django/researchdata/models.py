from django.conf import settings
from django.core.mail import send_mail
from django.db import models
import logging

logger = logging.getLogger(__name__)


class Sound(models.Model):
    """
    A Sound that a member of public shares with the project
    """

    sound = models.FileField(
        upload_to='researchdata/sounds/',
        help_text="Please upload your sound recording here.<br> If you're using Android or iOS and require help, please <a href=''>see the help guides</a>"
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Please provide some brief information about where you made the recording - e.g. a suburb in Kyiv, etc."
    )
    recording_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="date of recording",
        help_text="Please provide the date that the sound recording was produced"
    )
    recording_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name="time of recording",
        help_text="Please provide the time that the sound recording was produced (approximate hour, if exact time not known)"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Please provide any important information about the recording - e.g. the main sounds that it captures, your feelings about the recording, etc."
    )
    created = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sound #{self.id}: created {self.created}"
