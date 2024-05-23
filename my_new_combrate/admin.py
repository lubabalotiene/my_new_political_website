# admin.py

from django.contrib import admin
from .models import RegistrationLink, LoginButton

# Register your models here.

admin.site.register(RegistrationLink)
admin.site.register(LoginButton)
