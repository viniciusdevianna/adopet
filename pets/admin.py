from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile, Pet, Shelter, Adoption

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
    list_display = ('id', 'name', 'species', 'age', 'size', 'shelter', 'tutor')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'shelter', 'tutor')
    list_per_page = 15
    list_filter = ('species', 'size')
    ordering = ('name',)

class ShelterAdmin(admin.ModelAdmin):
    list_display = ('id', 'shelter_name', 'shelter_state', 'profile', 'date_registered')
    list_display_links = ('id', 'shelter_name')
    search_fields = ('shelter_name', 'profile')
    list_per_page = 15
    list_filter = ('shelter_state', 'date_registered')
    ordering = ('shelter_name',)

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'pet_shelter', 'tutor', 'date_registered', 'status')
    list_display_links = ('id',)
    search_fields = ('pet', 'pet_shelter', 'tutor')
    list_per_page = 15
    list_filter = ('status', 'date_registered')

    @admin.display()
    def pet_shelter(self, obj):
        return obj.pet.shelter.shelter_name

admin.site.register(Pet, PetAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Shelter, ShelterAdmin)
admin.site.register(Adoption, AdoptionAdmin)