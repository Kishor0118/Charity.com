from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    passw = models.CharField(max_length=128)
    membership_id = models.CharField(max_length=5, unique=True, editable=False)

    def generate_membership_id(self):
        last_user = UserInfo.objects.order_by('-id').first()
        if last_user:
            last_id = int(last_user.membership_id[1:])
            new_id = f'M{last_id + 1:04d}'  # Format the new ID with leading zeros
        else:
            new_id = 'M0001'  # Initial ID if no records exist
        return new_id

    def save(self, *args, **kwargs):
        if not self.membership_id:  # If Membership ID is not already set (i.e., for new instances)
            self.membership_id = self.generate_membership_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.membership_id}'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    passw = models.CharField(max_length=128)