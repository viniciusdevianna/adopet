from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Pet, Profile, Shelter, Adoption

class PetSerializer(serializers.ModelSerializer):
    species = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    first_trait = serializers.SerializerMethodField()
    second_trait = serializers.SerializerMethodField()
    tutor = serializers.ReadOnlyField(source='tutor.username')
    shelter = serializers.ReadOnlyField(source='shelter.shelter_name')

    def get_species(self, object):
        return object.get_species_display()
    def get_size(self, object):
        return object.get_size_display()
    def get_first_trait(self, object):
        return object.get_first_trait_display()
    def get_second_trait(self, object):
        return object.get_second_trait_display()
    
    class Meta:
        model = Pet
        fields = '__all__'

class ListTutorPetsSerializer(serializers.ModelSerializer):
    species = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    first_trait = serializers.SerializerMethodField()
    second_trait = serializers.SerializerMethodField()
    shelter = serializers.ReadOnlyField(source="shelter.shelter_name")

    def get_species(self, object):
        return object.get_species_display()
    def get_size(self, object):
        return object.get_size_display()
    def get_first_trait(self, object):
        return object.get_first_trait_display()
    def get_second_trait(self, object):
        return object.get_second_trait_display()
    
    class Meta:
        model = Pet
        exclude = ['tutor',]

class ListShelterPetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ['shelter', 'tutor']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'phone', 'city', 'state', 'about', 'is_tutor']

class ShelterSerializer(serializers.ModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.username')

    class Meta:
        model = Shelter
        fields = '__all__'

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'