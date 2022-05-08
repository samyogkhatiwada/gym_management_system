from django.db import models

# Create your models here.
class Contact(models.Model):
    name  = models.CharField(max_length=100)
    email  = models.EmailField()
    message  = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']