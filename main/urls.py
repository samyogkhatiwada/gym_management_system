import imp
from django.urls import path, include
from . import views
from .views import AddMember, Members, MemberDetail, Payment, AddTrainer, Trainers, CustomLogin, Dashboard, AddPayment, MemberDelete, TrainerDetail, MemberUpdate

from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('', Dashboard.as_view(), name='index'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('member', Members.as_view(), name='memberlist'),
    path('member/add', AddMember.as_view(), name='addmember'),
    path("member/<pk>", MemberDetail.as_view(), name="memberdetail"),
    path("member/update/<pk>", MemberUpdate.as_view(), name="memberupdate"),
    path("member/delete/<pk>", MemberDelete.as_view(), name="memberdelete"),
    path("payment", Payment.as_view(), name="payments"),
    path("payment/add", AddPayment.as_view(), name="addpayment"),
    path('trainer', Trainers.as_view(), name='trainerlist'),
    path('trainer/add', AddTrainer.as_view(), name='addtrainer'),
    path('trainer/<pk>', TrainerDetail.as_view(), name='trainerdetail'),
    
]
