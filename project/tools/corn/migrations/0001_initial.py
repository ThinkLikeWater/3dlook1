# Generated by Django 3.0.3 on 2020-11-29 22:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('uuiid', models.UUIDField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(upload_to='photos')),
                ('rotate_duration', models.FloatField()),
                ('d', models.CharField(max_length=123)),
            ],
        ),
    ]
