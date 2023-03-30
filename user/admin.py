from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import BrazilState, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-registering UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Registering BrazilState
admin.site.register(BrazilState)

