from django.db import models

class RegisterForm(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.EmailField()

    class Meta:
        db_table='datas'
        

# Create your models here.
