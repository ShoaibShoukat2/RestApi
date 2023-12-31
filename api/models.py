from django.db import models

# Create your models here.

departments = (
    ('IT','IT'),
    ('Non IT','Non IT'),
    ('Mobiles Phones','Mobile Phones'),

)

# Company Model

class Company(models.Model):
    comapny_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about =  models.TextField()
    type = models.CharField(max_length=100,choices=departments)
    addded_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name +'--'+ self.location        

# Employee model

choice = (
    ('Manager','manager'),
    ('Software Developer','sd'),
    ('Project Leader','pl'),
    ('Project Leader','pl')
)

class Employee(models.Model):
    name =  models.CharField(max_length=100)
    email =  models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about =  models.TextField()
    position = models.CharField(max_length=50,choices=choice)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
