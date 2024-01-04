
from django.contrib import admin
from django.urls import path,include
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crud.urls')),
]
