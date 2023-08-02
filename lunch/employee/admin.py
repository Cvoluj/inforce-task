from django.contrib import admin
from employee.models import Employee
from django.contrib.auth.admin import UserAdmin

admin.site.register(Employee, UserAdmin)
# Register your models here.
