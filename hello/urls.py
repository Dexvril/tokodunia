from django.contrib.auth import views as auth_views
from django.urls import path
from .views import hello_world
from .views import register
from .views import katalog
from .views import tambah_barang
from .views import edit_barang
from .views import hapus_barang
from django.conf import settings 
from django.conf.urls.static import static  

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('katalog/', katalog, name='katalog'),
    path('templates/tambah_barang.html/', tambah_barang, name='tambah_barang'),
    path('katalog/edit/<int:pk>/', edit_barang, name='edit_barang'),
    path('katalog/hapus/<int:pk>/', hapus_barang, name='hapus_barang'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



