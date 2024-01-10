from django.contrib import admin
from .models import Cards
# Register your models here.

@admin.register(Cards)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "front", "back"]
