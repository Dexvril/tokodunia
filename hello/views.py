from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login  # Pastikan login di-import
from .models import Product
from .forms import RegisterForm, ProductForm
from django.db import connection

# ---------------------------------------------------------------------------------
# Contoh view sederhana untuk "Hello, World!" tanpa autentikasi
def hello_world_public(request):
    return HttpResponse("Hello, World!")

# ---------------------------------------------------------------------------------
# View untuk "Hello, World!" dengan autentikasi (hanya user yang sudah login)
@login_required
def hello_world(request):
    return render(request, 'hello.html')

# ---------------------------------------------------------------------------------
# View untuk proses registrasi user
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Simpan user dengan password yang sudah di-hash
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # Login otomatis setelah registrasi
            return redirect('home')  # Ganti 'home' dengan nama URL halaman tujuan
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# ---------------------------------------------------------------------------------
# View untuk menampilkan halaman katalog produk
def katalog(request):
    products = Product.objects.all()  # Mengambil semua data produk
    return render(request, 'katalog.html', {'products': products})

# ---------------------------------------------------------------------------------
# View untuk menambahkan produk baru
def tambah_barang(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("katalog")  # Redirect ke halaman katalog setelah produk ditambahkan
    else:
        form = ProductForm()
    return render(request, "tambah_barang.html", {"form": form})

# ---------------------------------------------------------------------------------
# View untuk mengedit produk yang sudah ada
def edit_barang(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('katalog')  # Pastikan redirect menggunakan nama URL yang benar
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_barang.html', {'form': form, 'product': product})

# ---------------------------------------------------------------------------------
# View untuk menghapus produk
def hapus_barang(request, barang_id):
    barang = get_object_or_404(Product, id=barang_id)
    barang.delete()
    return redirect('katalog')
