# Generated by Django 2.1.7 on 2019-05-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_conditioner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=16)),
                ('operation', models.CharField(max_length=32)),
                ('op_time', models.DateTimeField()),
            ],
        ),
    ]
