from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pets', views.PetsViewSet, basename='pets')
router.register('tutors', views.ProfilesViewSet, basename='tutors')

urlpatterns = [
    path('pets/', include(router.urls)),
    path('tutor/<int:pk>/pets/', views.ListTutorPets.as_view()),
]