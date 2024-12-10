# Generated by Django 4.2.16 on 2024-12-07 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0002_data_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='description_ukrainian',
            field=models.TextField(blank=True, null=True, verbose_name='Description (Ukrainian translation)'),
        ),
        migrations.AddField(
            model_name='sound',
            name='interviewee_reflection',
            field=models.TextField(blank=True, help_text="Following an interview with author of this sound, include interesting reflections they've had about their submission", null=True),
        ),
        migrations.AddField(
            model_name='sound',
            name='interviewee_reflection_ukrainian',
            field=models.TextField(blank=True, null=True, verbose_name='Interviewee reflection (Ukrainian translation)'),
        ),
        migrations.AddField(
            model_name='sound',
            name='location_soundscape_exhibition',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location shown publicly in the soundscape exhibition'),
        ),
        migrations.AddField(
            model_name='sound',
            name='location_soundscape_exhibition_ukrainian',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location shown publicly in the soundscape exhibition (Ukrainian translation)'),
        ),
        migrations.AddField(
            model_name='sound',
            name='order_in_soundscape_exhibition',
            field=models.FloatField(default=0, help_text='Sounds will be shown in the public soundscape exhibition in order of this value from lowest to highest'),
        ),
        migrations.AddField(
            model_name='sound',
            name='photo',
            field=models.ImageField(blank=True, help_text='Please upload a photo related to this sound, to be shown on the public soundscape exhibition', null=True, upload_to='researchdata/photos/'),
        ),
        migrations.AddField(
            model_name='sound',
            name='prompt_for_public_comments',
            field=models.TextField(blank=True, help_text='Provide a prompt (i.e. a question or statement) to encourage users to comment on this in the public website', null=True),
        ),
        migrations.AlterField(
            model_name='sound',
            name='admin_approved',
            field=models.BooleanField(default=False, help_text="Please tick this box if you're happy for this sound to be included in the public sound exhibition."),
        ),
        migrations.CreateModel(
            name='SoundscapeExhibitionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('admin_approved', models.BooleanField(default=False, help_text="Sound data might be shared on the public website in the future. Please tick this box if you're happy for this sound to be included on the public website, if this feature is added in the future.")),
                ('sound', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='soundscape_exhibition_comment', to='researchdata.sound')),
            ],
        ),
        migrations.CreateModel(
            name='SoundsRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_details', models.TextField(blank=True, null=True)),
                ('sound_1', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sound_relationship_1', to='researchdata.sound')),
                ('sound_2', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sound_relationship_2', to='researchdata.sound')),
            ],
        ),
        migrations.AddField(
            model_name='sound',
            name='related_sounds',
            field=models.ManyToManyField(blank=True, through='researchdata.SoundsRelationship', to='researchdata.sound'),
        ),
    ]
