# Generated by Django 4.0.1 on 2022-01-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_skills_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='about',
            field=models.TextField(default='', max_length=800),
            preserve_default=False,
        ),
    ]
