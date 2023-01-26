from django.contrib import admin
from main.models import  Task

# Register your models here.

from .models import *

admin.site.register(Task)
