from django.contrib import admin
from .models import Profile,Service,UsingPlan

# Register your models here.

admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(UsingPlan)