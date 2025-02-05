from django.contrib.auth import views as auth_views
from django.urls import path
from .views import hello_world
from .views import register
from .views import katalog
from .views import katalog, tambah_barang, edit_barang, hapus_barang

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('katalog/', katalog, name='katalog'),
    path('katalog/tambah/', tambah_barang, name='tambah_barang'),
    path('katalog/edit/<int:pk>/', edit_barang, name='edit_barang'),
    path('katalog/hapus/<int:pk>/', hapus_barang, name='hapus_barang'),
]




