from audioop import reverse
import imp
from operator import mod
from pyexpat import model
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView, TemplateView
from .models import Member, Trainer, Payment
from home.models import Contact
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# login view 
class CustomLogin(LoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True

# Dashboard View 
class Dashboard(LoginRequiredMixin, TemplateView):

    template_name = "main/index.html"
# Add Member 
class AddMember(LoginRequiredMixin, CreateView):
    model = Member
    template_name = "main/member_form.html"
    fields = '__all__'
    def get_success_url(self):
        agent_id = self.object.id
        return reverse_lazy('memberdetail', kwargs={'pk': agent_id})
class AddPayment(LoginRequiredMixin, CreateView):
    model = Payment
    success_url = reverse_lazy('trainerlist')
    fields = '__all__'

class Members(LoginRequiredMixin, ListView):
    model = Member
    context_object_name= 'customerlist'

class MemberDetail(LoginRequiredMixin, DetailView):
    model = Member
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['payments'] = instance.payment_set.all()
        return context
    context_object_name= 'customer'

class AddTrainer(LoginRequiredMixin, CreateView):
    model = Trainer
    success_url = reverse_lazy('trainerlist')
    fields = '__all__'
    
class Trainers(LoginRequiredMixin, ListView):
    model = Trainer
    context_object_name= 'trainerlist'

class Payment(LoginRequiredMixin, ListView):
    model = Payment
    context_object_name= 'payments'


class Messages(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'messages'
    template_name = "main/contact_list.html"
