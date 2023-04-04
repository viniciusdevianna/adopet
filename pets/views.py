from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from .models import Pet, Profile, Shelter, Adoption

class PetsViewSet(viewsets.ModelViewSet):
    """Show all available pets"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializer    

class ProfilesViewSet(viewsets.ModelViewSet):
    """Show all tutors registered"""
    def get_queryset(self):
        return Profile.objects.filter(is_tutor=1)
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

class SheltersViewSet(viewsets.ModelViewSet):
    """Show all shelters registered"""
    queryset = Shelter.objects.all()

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ShelterSerializer

class AdoptionsViewSet(viewsets.ModelViewSet):
    """Show all current registered adoptions"""
    queryset = Adoption.objects.all()

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.pet.shelter.profile:
            raise ValidationError("Apenas o abrigo pode cancelar uma adoção")
        instance.delete()

    serializer_class = AdoptionSerializer

class ListTutorPets(generics.ListAPIView):
    """List all pets registered under specified tutor"""
    def get_queryset(self):
        return Pet.objects.filter(tutor=self.kwargs['pk'])
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListTutorPetsSerializer


class ListShelterPets(generics.ListAPIView):
    """List all pets registered under specified shelter"""
    def get_queryset(self):
        return Pet.objects.filter(shelter=self.kwargs['pk'])
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListShelterPetsSerializer