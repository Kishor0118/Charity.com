from django.contrib import admin
from .models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname', 'gender', 'dob', 'address', 'city', 'state', 'country', 'zip_code', 'phone', 'email','membership_id']

admin.site.register(UserInfo, UserInfoAdmin)


