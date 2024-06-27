from django.db import models
from django.core.validators import validate_email


# Create your models here.

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False)
    location=models.CharField(max_length=100)
    def __str__(self) :
        return self.name

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False)
    def __str__(self) :
        return self.name



class Employee(models.Model):
    first_name=models.CharField(max_length=50, null=False)
    last_name=models.CharField( max_length=50)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    phone=models.BigIntegerField(default=True)
    hire_date=models.DateField()
    def __str__(self) :
        return self.first_name + self.last_name
    
    
class MyAuthentication(models.Model):
    Username= models.CharField( max_length=50)
    Password = models.CharField(max_length=10)
    Email = models.EmailField( max_length=254, validators=[validate_email])
    Phone = models.CharField(max_length=10, default=None)
    
    
class Otp(models.Model):
    Email = models.EmailField(max_length=254, default=None)
    User_otp = models.IntegerField()
    