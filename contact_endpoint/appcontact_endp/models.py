from django.db import models

class category_choices(models.TextChoices):

    IMPORTANT = "Important", "Important"
    FIRE_DEPARTMENT = "Fire Department", "Fire Department"
    HOSPITAlS = "Hospitals", "Hospitals"
    SHELTERS = "Shelters", "Shelters"

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    hotline = models.CharField(max_length=20)
    category = models.CharField(
        max_length=50,
        choices=category_choices.choices
        )
    
def __str__(self):
    return f"{self.name} -  {self.category}" 

