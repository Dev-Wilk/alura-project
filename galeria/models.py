from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPTIONS_CATEGORY = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    name = models.CharField(max_length= 100, null= False, blank= False)
    legend = models.CharField(max_length= 100, null= False, blank= False)
    category = models.CharField(max_length=50, choices=OPTIONS_CATEGORY, default='')
    description = models.TextField(null= False, blank= False)
    photo = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    visible = models.BooleanField(default=False)
    date_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name
    