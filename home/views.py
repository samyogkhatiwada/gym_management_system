from django.shortcuts import render
from .models import Contact
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'home/index.html')
