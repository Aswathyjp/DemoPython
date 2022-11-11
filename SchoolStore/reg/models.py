from django.db import models

# Create your models here.
class dispform(models.Model):
    username=models.CharField(max_length=250)
    age = models.IntegerField()
    address=models.CharField(max_length=250)
    def __str__(self):
        return self.username