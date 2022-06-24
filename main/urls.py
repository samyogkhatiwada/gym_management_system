import imp
from django.urls import path, include
from . import views
from .views import AddMember, Members, MemberDetail, Payment, AddTrainer, Trainers, CustomLogin, Dashboard, AddPayment, MemberDelete, TrainerDetail, MemberUpdate, createPlan, Plans

from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('', Dashboard.as_view(), name='index'), # Dashboard url
    path('login/', CustomLogin.as_view(), name='login'), #login url
    path('logout/', LogoutView.as_view(), name='logout'), #logout url
    path('member/add', AddMember.as_view(), name='addmember'), #member add url
    path("member/<pk>", MemberDetail.as_view(), name="memberdetail"), #member detail url
    path('member', Members.as_view(), name='memberlist'), #member list url
    path("member/update/<pk>", MemberUpdate.as_view(), name="memberupdate"), #member update url
    path("member/delete/<pk>", MemberDelete.as_view(), name="memberdelete"), #member delete url
    path('trainer/add', AddTrainer.as_view(), name='addtrainer'), #trainer add url
    path('trainer/<pk>', TrainerDetail.as_view(), name='trainerdetail'), #trainer detail url
    path('trainer', Trainers.as_view(), name='trainerlist'), #trainer list url
    path("payment", Payment.as_view(), name="payments"), #payment list url
    path("payment/add", AddPayment.as_view(), name="addpayment"), #payment add url
    path('plan/', Plans.as_view(), name='plans'), #plan list url
    path('plan/add', createPlan.as_view(), name='addplan'), #plan add url
    
]
