from rest_framework import viewsets, generics
from .serializer import PetSerializer, ListTutorPetsSerializer, ProfileSerializer
from .models import Pet, Profile

class PetsViewSet(viewsets.ModelViewSet):
    """Show all available pets"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class ProfilesViewSet(viewsets.ModelViewSet):
    """Show all tutors registered"""
    def get_queryset(self):
        return Profile.objects.filter(is_tutor=1)
    
    serializer_class = ProfileSerializer

class ListTutorPets(generics.ListAPIView):
    """List all pets registered under specified tutor"""
    def get_queryset(self):
        return Pet.objects.filter(tutor=self.kwargs['pk'])
    
    serializer_class = ListTutorPetsSerializer

