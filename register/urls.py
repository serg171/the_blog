from django.urls import path, include
from .views import RegisterFormView
from django.contrib.auth import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', RegisterFormView.as_view(), name='register')
]
