# Generated by Django 4.2 on 2024-03-31 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=128)),
            ],
        ),
    ]
