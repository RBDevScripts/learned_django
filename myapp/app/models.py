from django.db import models

# Create your models here.
class Reg(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    dob=models.DateTimeField()
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.name
