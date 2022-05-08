from django.db import models
import uuid

class Member(models.Model):
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    joining_date = models.DateField()
    trainer = models.ForeignKey('Trainer',  on_delete=models.CASCADE, blank=True)
    GENDER = (
        ('m', 'male'),
        ('f', 'female'),
        ('o', 'others'),
    )
    gender = models.CharField(
        max_length=1,
        choices= GENDER,
        blank=True,
        
    )
    def __str__(self):
        
        return self.fullName
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
    description = models.TextField()
    date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.description