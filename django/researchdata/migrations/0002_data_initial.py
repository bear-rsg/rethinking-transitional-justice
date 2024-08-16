from django.db import migrations
from .. import models
import random


def insert_sound_upload_codes(apps, schema_editor):
    """
    Inserts 50 new randomly generated, unique sound upload codes
    """

    # Create list of SoundUploadCode objects, each with a unique 6 digit code
    sound_upload_codes = []
    for i in range (50):
        while True:
            code = str(random.randint(100000, 999999))
            if code not in sound_upload_codes:
                sound_upload_codes.append(models.SoundUploadCode(code=code))
                break
    # Bulk create objects
    models.SoundUploadCode.objects.bulk_create(sound_upload_codes)


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_sound_upload_codes)
    ]
