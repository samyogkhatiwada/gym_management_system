import imp
from django.urls import path, include
from . import views
from .views import AddMember, Members, MemberDetail, Payment, AddTrainer, Trainers, Messages, CustomLogin, Dashboard, AddPayment

from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('', Dashboard.as_view(), name='index'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('member', Members.as_view(), name='memberlist'),
    path('member/add', AddMember.as_view(), name='addmember'),
    path("member/<pk>", MemberDetail.as_view(), name="memberdetail"),
    path("payment", Payment.as_view(), name="payments"),
    path("payment/add", AddPayment.as_view(), name="addpayment"),
    path('trainer/add', AddTrainer.as_view(), name='addtrainer'),
    path('trainer', Trainers.as_view(), name='trainerlist'),
    path('message', Messages.as_view(), name='messagelist'),
    
]
