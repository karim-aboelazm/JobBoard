# Generated by Django 4.0.1 on 2022-01-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_candidate_applying'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobowner',
            name='company_not_ex',
        ),
        migrations.AlterField(
            model_name='candidates',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='candidate_resumes/'),
        ),
    ]
