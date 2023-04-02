from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class Profile(AbstractUser):
    IS_TUTOR = [
        (0, 'Não'),
        (1, 'Sim')
    ]

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

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES, default='RJ')
    about = models.CharField(max_length=480, blank=True)
    is_tutor = models.IntegerField(choices=IS_TUTOR, default=0)

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
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

    tutor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

