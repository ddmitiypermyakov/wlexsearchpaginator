from django.contrib import admin

# Register your models here.
from .models import Trainig

class TrainigAdmin(admin.ModelAdmin):
    list_display =('title', 'quantity','distance','date')
    list_filter = ('title', 'quantity','distance')
    search_fields = ('title', 'quantity','distance')


    fields = ('title', 'quantity','distance')

admin.site.register(Trainig, TrainigAdmin)