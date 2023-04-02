from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile, Pet

class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ('username', 'email', 'state', 'is_active', 'is_tutor')
    list_filter = ('city', 'is_active', 'is_staff', 'is_tutor')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Location', {'fields': ('city', 'state')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_tutor', 'groups', 'user_permissions')}),
    )

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'age', 'size', 'tutor')
    list_display_links = ('id', 'name', 'tutor')
    search_fields = ('name', 'tutor')
    list_per_page = 15
    list_filter = ('species', 'size')


admin.site.register(Pet, PetAdmin)
admin.site.register(Profile, ProfileAdmin)

