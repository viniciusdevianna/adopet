from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import Pet, Profile, Shelter, Adoption

class PetsViewSet(viewsets.ModelViewSet):
    """Show all available pets"""
    def get_queryset(self):
        return Pet.objects.filter(adopted=False)
    
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name',]
    search_fields = ['name',]
    filterset_fields = ['species',]

class ProfilesViewSet(viewsets.ModelViewSet):
    """Show all tutors registered"""
    def get_queryset(self):
        return Profile.objects.filter(is_tutor=1)
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['username',]
    search_fields = ['username', 'email']
    filterset_fields = ['state',]

class SheltersViewSet(viewsets.ModelViewSet):
    """Show all shelters registered"""
    queryset = Shelter.objects.all()

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ShelterSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['shelter_name',]

class AdoptionsViewSet(viewsets.ModelViewSet):
    """Show all current registered adoptions"""
    queryset = Adoption.objects.all()

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if not self.request.user.is_superuser:
            raise ValidationError("Apenas o admin pode deletar uma adoção")
        instance.delete()

    def perform_update(self, serializer):
        if serializer.validated_data['status'] == 'R':
            adopted_pet_id = serializer.validated_data['pet'].id
            update_pet_adoption_status(adopted_pet_id)

        if serializer.validated_data['status'] == 'C':
            if self.request.user != serializer.validated_data['pet'].shelter.profile:
                raise ValidationError("Apenas o abrigo responsável pode cancelar uma adoção")
        
        serializer.save()

    serializer_class = AdoptionSerializer

class ListTutorPets(generics.ListAPIView):
    """List all pets registered under specified tutor"""
    def get_queryset(self):
        return Pet.objects.filter(tutor=self.kwargs['pk'])
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListTutorPetsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name',]


class ListShelterPets(generics.ListAPIView):
    """List all pets registered under specified shelter"""
    def get_queryset(self):
        return Pet.objects.filter(shelter=self.kwargs['pk'])
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListShelterPetsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['shelter_name',]

# Utility functions

def update_pet_adoption_status(pet_id):
    pet = Pet.objects.get(pk=pet_id)
    pet.update_adoption_status()
    pet.save()