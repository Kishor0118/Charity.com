# Generated by Django 4.2 on 2024-03-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0014_alter_userinfo_membership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='membership_id',
            field=models.CharField(editable=False, max_length=5, unique=True),
        ),
    ]
