from django.contrib import admin
from .models import People
# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('NID', 'TITLE','F_NAME', 'L_NAME')
    fields = ['F_NAME', 'L_NAME']
    
    

admin.site.register(People,PeopleAdmin) 