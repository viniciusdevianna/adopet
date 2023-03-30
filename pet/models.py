from django.db import models
from user.models import Profile
from django.utils.translation import gettext_lazy as _

class Pet(models.Model):

    class Sizes(models.IntegerChoices):
        MINI = 0
        SM = 1
        SM_MD = 2
        MD = 3
        MD_BG = 4
        BG = 5
        XL = 6

    class Traits(models.IntegerChoices):
        ACTIVE = 0
        CALM = 1
        POLITE = 2
        PLAYFUL = 3
        TENDER = 4
        KIND = 5

    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(default=0)
    size = models.IntegerField(default=0, choices=Sizes.choices)
    first_trait = models.IntegerField(default=0, choices=Traits.choices)
    second_trait = models.IntegerField(default=0, choices=Traits.choices)

    tutor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)


