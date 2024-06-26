# Generated by Django 4.2.13 on 2024-05-22 21:25

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('url', models.URLField()),
                ('ranking', models.IntegerField(choices=[(1, 'MINIMUM'), (2, 'MEH'), (3, 'AVERAGE'), (4, 'AMAZING'), (5, 'PERFECT')], default=jobs.models.Ranking['AVERAGE'])),
            ],
        ),
    ]
