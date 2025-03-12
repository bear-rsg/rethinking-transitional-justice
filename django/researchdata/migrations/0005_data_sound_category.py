from django.db import migrations
from .. import models


def insert_sound_categories(apps, schema_editor):
    """
    Inserts initial sound categories, provided by Janine
    """

    # Create list of SoundUploadCode objects, each with a unique 6 digit code
    sound_categories = [
        {
            'name': "New sounds / sonic intrusiveness of war",
            'name_ukrainian': "Нові звуки/звукова нав’язливість війни",
            'order': 1.0,
        },
        {
            'name': "Animal experiences of war",
            'name_ukrainian': "Досвід тварин під час війни",
            'order': 2.0,
        },
        {
            'name': "Living with power shortages",
            'name_ukrainian': "Життя з відключеннями електр",
            'order': 3.0,
        },
        {
            'name': "A brief respite from war",
            'name_ukrainian': "Короткий перепочинок від війни",
            'order': 4.0,
        },
        {
            'name': "Some reflections on war",
            'name_ukrainian': "Деякі роздуми про війну",
            'order': 5.0,
        },
        {
            'name': "Missed sounds",
            'name_ukrainian': "Звуки, яких не вистачає",
            'order': 6.0,
        },
        {
            'name': "Listening to the sounds of Nature",
            'name_ukrainian': "Слухаючи звуки природи",
            'order': 7.0,
        },
        {
            'name': "Hope for the future",
            'name_ukrainian': "Надія на майбутнє",
            'order': 8.0,
        },
    ]

    # Create objects
    for sound_category in sound_categories:
        models.SoundCategory.objects.create(**sound_category)


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0004_soundcategory_sound_category'),
    ]

    operations = [
        migrations.RunPython(insert_sound_categories)
    ]
