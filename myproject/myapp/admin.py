from django.contrib import admin
from .models import posttable

class Testadmin(admin.ModelAdmin):
    model=posttable
    list_diaplay=['Emp_id','Emp_name']
    search_fields=['Emp_id']
admin.site.register(posttable, Testadmin)
# Register your models here.
