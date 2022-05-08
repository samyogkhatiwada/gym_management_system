
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('home.urls')),
    path('admin/', include('main.urls'))
]
