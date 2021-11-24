from django.db import models
class instructorinfo(models.Model):
    fullname = models.CharField(max_length=128, null=True)
    gender = models.CharField(max_length=128, null=True)
    number = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=128,null=True)
    bio = models.TextField(null=True)
    

    def __str__(self) -> str:
        return self.fullname    


# Create your models here.
