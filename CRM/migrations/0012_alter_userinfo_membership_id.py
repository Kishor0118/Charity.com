# Generated by Django 4.2 on 2024-03-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0011_alter_userinfo_membership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='membership_id',
            field=models.CharField(default='M0001', editable=False, max_length=10, unique=True),
        ),
    ]