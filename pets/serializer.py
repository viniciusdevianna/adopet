from rest_framework import serializers
from .models import Pet, Profile

class PetSerializer(serializers.ModelSerializer):
    species = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    first_trait = serializers.SerializerMethodField()
    second_trait = serializers.SerializerMethodField()
    tutor = serializers.ReadOnlyField(source='tutor.username')

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

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'phone', 'city', 'state', 'about', 'is_tutor']