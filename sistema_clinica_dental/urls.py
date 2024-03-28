from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
     # URL para el Login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # URL para el Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
