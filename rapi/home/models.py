from django.db import models
class Emp(models.Model):
    ename=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    email=models.EmailField(max_length=200)
    def __str__(self) -> str:
        return self.ename
# Create your models here.
