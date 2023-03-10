# Generated by Django 4.0.6 on 2022-09-13 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_clip', models.CharField(blank=True, max_length=200, null=True, verbose_name='비디오 클립')),
                ('video_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='비디오 url')),
                ('level', models.CharField(max_length=100, verbose_name='상태')),
                ('datetime', models.DateTimeField(verbose_name='날짜')),
                ('profile', models.ForeignKey(blank=True, db_column='profile', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtsp_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='rtsp url')),
                ('profile', models.ForeignKey(blank=True, db_column='profile', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
