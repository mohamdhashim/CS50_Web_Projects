from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from .models import *
# Register your models here.

admin.site.register(Email)
admin.site.register(User)