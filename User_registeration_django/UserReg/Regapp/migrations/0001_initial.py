# Generated by Django 5.0.4 on 2024-05-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
