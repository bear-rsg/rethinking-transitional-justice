from django.conf import settings
from django import forms
from . import models
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.DateInput):
    input_type = 'time'


class SoundCreateForm(forms.ModelForm):
    """
    A form for users to submit a 'Sound' object
    """

    # Sound Upload Code (prevents unwanted people from uploading sound data)
    sound_upload_code = forms.CharField(
        label='Sound Upload Code',
        help_text="The 6 digit code provided to you by the research team that's required to upload sound data. Contact us for help if you're unsure."
    )

    # Google ReCaptcha
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Sound
        fields = (
            'sound_upload_code',
            'sound',
            'location',
            'recording_date',
            'recording_time',
            'description',
        )
        widgets = {
            'recording_date': DateInput(),
            'recording_time': TimeInput(),
        }

    def clean_sound_upload_code(self):
        """
        Ensure that the sound_upload_code matches the code defined in the settings.
        If not, show error.
        """
        cleaned_data = self.clean()
        sound_upload_code = cleaned_data.get('sound_upload_code')
        if sound_upload_code != settings.SOUND_UPLOAD_CODE:
            self.add_error(
                'sound_upload_code',
                "The sound upload code is not valid. Please contact us for help if needed."
            )
        return sound_upload_code
