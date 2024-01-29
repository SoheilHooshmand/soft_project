from django.contrib import admin

# Register your models here.
from .models import Profile, Lawyer, Client, Expertise
admin.site.register(Profile)
admin.site.register(Lawyer)
admin.site.register(Client)
admin.site.register(Expertise)