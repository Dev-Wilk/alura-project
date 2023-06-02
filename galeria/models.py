from django.db import models

class Fotografia(models.Model):
    name = models.CharField(max_length= 100, null= False, blank= False)
    legend = models.CharField(max_length= 100, null= False, blank= False)
    description = models.TextField(null= False, blank= False)
    photo = models.CharField(max_length= 100, null= False, blank= False)

    def __str__(self):
        return f"Fotografia [name={self.name}]"
    