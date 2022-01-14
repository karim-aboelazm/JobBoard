# Generated by Django 4.0.1 on 2022-01-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobs_benefits_jobs_location_jobs_logo_jobs_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='bio',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidates',
            name='english_level',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced'), ('expert', 'expert')], default='beginner', max_length=50),
        ),
        migrations.AddField(
            model_name='candidates',
            name='experience',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced'), ('expert', 'expert')], default='beginner', max_length=50),
        ),
        migrations.AddField(
            model_name='candidates',
            name='hour_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='candidates',
            name='profession',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidates',
            name='projects_num',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.candidates')),
            ],
        ),
    ]
