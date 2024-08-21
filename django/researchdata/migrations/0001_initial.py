# Generated by Django 4.2.15 on 2024-08-16 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoundUploadCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('assigned_to', models.CharField(blank=True, help_text='Input identifying information about which user this code has been assigned to (e.g. name, email)', max_length=255, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.FileField(help_text='Please upload your sound recording here<br>Будь ласка завантажте Ваш звукозапис сюди', upload_to='researchdata/sounds/', verbose_name='Sound / Звук')),
                ('location', models.CharField(blank=True, help_text='Please provide some brief information about where you made the recording - e.g. a suburb in Kyiv, etc.<br>Надайте коротку інформацію про те, де ви зробили запис, напр. передмістя в м. Києві тощо', max_length=255, null=True, verbose_name='location / Локація')),
                ('recording_date', models.DateField(blank=True, help_text='Please provide the date that the sound recording was produced<br>Будь ласка, вкажіть дату створення звукозапису.', null=True, verbose_name='date of recording / Дата запису')),
                ('recording_time', models.TimeField(blank=True, help_text='Please provide the time that the sound recording was produced (approximate hour, if exact time not known)<br>Будь ласка, вкажіть час, коли було створено звукозапис (приблизну годину доби, якщо точний час невідомий)', null=True, verbose_name='time of recording / Час запису')),
                ('description', models.TextField(blank=True, help_text='Please provide any important information about the recording - e.g. the main sounds that it captures, your feelings about the recording, etc.<br> Будь ласка, надайте будь-яку інформацію про запис – напр. основні звуки, які він вловлює, ваші почуття щодо запису тощо.', null=True, verbose_name='description / Опис')),
                ('admin_approved', models.BooleanField(default=False, help_text="Sound data might be shared on the public website in the future. Please tick this box if you're happy for this sound to be included on the public website, if this feature is added in the future.")),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sound_upload_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sounds', to='researchdata.sounduploadcode')),
            ],
        ),
    ]
