from django.contrib import admin

# Register your models here.
from .models import Trainig

class TrainigAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trainig, TrainigAdmin)