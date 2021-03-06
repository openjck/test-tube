# Generated by Django 2.0.5 on 2018-06-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_confidence_intervals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('experiment', models.CharField(max_length=255)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('window_start', models.DateTimeField()),
                ('window_end', models.DateTimeField()),
                ('enroll_count', models.IntegerField()),
                ('unenroll_count', models.IntegerField()),
            ],
        ),
    ]
