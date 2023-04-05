from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from .managers import CustomUserManager

STATES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

class Profile(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES, default='RJ')
    about = models.CharField(max_length=480, blank=True)
    is_tutor = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class Shelter(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    shelter_name = models.CharField(max_length=150)
    shelter_city = models.CharField(max_length=100)
    shelter_state = models.CharField(max_length=2, choices=STATES, default='RJ')
    shelter_address = models.CharField(max_length=240, blank=True)
    shelter_about = models.CharField(max_length=480, blank=True)

    date_registered = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.shelter_name

    
class Pet(models.Model):
    
    class Sizes(models.TextChoices):
        MINI = 'MIN', _('Mini')
        SM = 'SMA', _('Pequeno')
        SM_MD = 'SMD', _('Pequeno/Médio')
        MD = 'MED', _('Médio')
        MD_BG = 'MDB', _('Médio/Grande')
        BG = 'BIG', _('Grande')
        XL = 'VBG', _('Enorme')

    class Traits(models.TextChoices):
        ACTIVE = 'ACT', _('Ativo')
        CALM = 'CAL', _('Calmo')
        POLITE = 'POL', _('Educado')
        PLAYFUL = 'PLA', _('Brincalhão')
        TENDER = 'TEN', _('Carinhoso')
        KIND = 'KIN', _('Gentil')

    class Species(models.TextChoices):
        DOG = 'D', _('Cão')
        CAT = 'C', _('Gato')
        BIRD = 'B', _('Pássaro')
        OTHER = 'O', _('Outra')

    name = models.CharField(max_length=150)
    species = models.CharField(max_length=1, default='D', choices=Species.choices)
    age = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=3, default='MIN', choices=Sizes.choices)
    first_trait = models.CharField(max_length=3, default='ACT', choices=Traits.choices, blank=True)
    second_trait = models.CharField(max_length=3, default='ACT', choices=Traits.choices, blank=True)

    tutor = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.DO_NOTHING, null=True)
    
    adopted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class Adoption(models.Model):
    STATUS = [
        ('A', 'Em andamento'),
        ('R', 'Realizada'),
        ('C', 'Cancelada')
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    date_finished = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self) -> str:
        return f'Adoção de {self.pet} por {self.tutor}'


