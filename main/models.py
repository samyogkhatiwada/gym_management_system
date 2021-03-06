from django.db import models
from django.utils import timezone
import uuid
class Member(models.Model):  
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    joining_date = models.DateField(default=timezone.now)
    trainer = models.ForeignKey('Trainer',  on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='member/')
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Others', 'others'),
    )
    gender = models.CharField(
        max_length=10,
        choices= GENDER,
        blank=True,
        
    )
    description = models.TextField()
    def __str__(self):
        
        return self.fullName + ' - ' + f'{self.id}'

class Trainer(models.Model):
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.TextField()
    def __str__(self) -> str:
        return self.fullName

class Payment(models.Model):
    member = models.ForeignKey('Member',  on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.ForeignKey('Plan', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now= True)
    month = models.CharField(
        max_length=100,
        
    )
    description = models.TextField()
    def __str__(self):
        return self.description
        
class Plan(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    def __str__(self):
        return self.title