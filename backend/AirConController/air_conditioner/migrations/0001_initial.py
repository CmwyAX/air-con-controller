# Generated by Django 2.1.7 on 2019-05-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('detail_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_id', models.CharField(max_length=16)),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('speed', models.IntegerField()),
                ('fee_rate', models.FloatField()),
                ('fee', models.FloatField()),
            ],
        ),
    ]
