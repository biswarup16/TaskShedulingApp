from django.contrib import admin

from app.models import TODO

# Register your models here.
@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ['title','status','user','date','priority']
