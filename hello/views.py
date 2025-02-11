from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm



def hello_world(request):
    return HttpResponse("Hello, World!")
@login_required
def hello_world(request):
    return render(request, 'hello.html')
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save()
            login(request, user)
            return redirect('home')  # Ganti dengan halaman tujuan setelah register
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
def katalog(request):
    products = Product.objects.all()
    return render(request, 'katalog.html', {'products': products})

# Menampilkan katalog
def katalog(request):
    products = Product.objects.all()
    return render(request, 'katalog.html', {'products': products})

def tambah_barang(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("katalog")  # Sesuaikan dengan nama URL katalog
    else:
        form = ProductForm()
    return render(request, "tambah_barang.html", {"form": form})



# Edit Barang
def edit_barang(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('templates/katalog')
    else:
        form = ProductForm(instance=product)
    return render(request, 'templates/edit_barang.html', {'form': form, 'product': product})

def hapus_barang(request, barang_id):
    barang = get_object_or_404(Product, id=barang_id)
    barang.delete()
    return redirect('katalog')