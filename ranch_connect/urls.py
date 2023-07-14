from django.contrib import admin
from django.urls import path
from FazendaAltoParaiso import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
]
