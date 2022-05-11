from audioop import reverse
from dataclasses import fields
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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context['notrainers'] = len(Trainer.objects.all()) 
    #     context['nomembers'] = len(Member.objects.all()) 
    #     return context
    template_name = "main/index.html"
# Add Member 
class AddMember(LoginRequiredMixin, CreateView):
    model = Member
    template_name = "main/member_form.html"
    fields = '__all__'
    def get_success_url(self):
        agent_id = self.object.id
        return reverse_lazy('memberdetail', kwargs={'pk': agent_id})
class AddTrainer(LoginRequiredMixin, CreateView):
    model = Trainer
    success_url = reverse_lazy('trainerlist')
    fields = '__all__'
# Add Payment 
class AddPayment(LoginRequiredMixin, CreateView):
    model = Payment
    success_url = reverse_lazy('payments')
    fields = '__all__'
# Members List 
class Members(LoginRequiredMixin, ListView):
    model = Member
    context_object_name= 'customerlist'
# Member Detail
class MemberDetail(LoginRequiredMixin, DetailView):
    model = Member
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['payments'] = instance.payment_set.all()
        return context
    context_object_name= 'customer'
#  member delete
class MemberUpdate(LoginRequiredMixin, UpdateView):
    model = Member
    fields = [
        "fullName",
        "address",
        "plan",
        "email",
        "contact",
        "photo",
        "trainer",
    ]
    context_object_name= 'customer'
    template_name = "main/member_update.html"

  
# member delete
class MemberDelete(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('member')

# trainer list
class Trainers(LoginRequiredMixin, ListView):
    model = Trainer
    context_object_name= 'trainerlist'
# trainer detail 
class TrainerDetail(LoginRequiredMixin, DetailView):
    model = Trainer
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['members'] = instance.member_set.all()
        return context
    context_object_name= 'trainer'
# transaction history
class Payment(LoginRequiredMixin, ListView):
    model = Payment
    
    context_object_name= 'payments'

# message history
class Messages(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'messages'
    template_name = "main/contact_list.html"
