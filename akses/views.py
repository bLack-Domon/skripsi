from django.shortcuts import render, redirect
from .models import Karyawan
from .forms import KaryawanForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login

# Create your views here.
@login_required(login_url='login')
@pilihan_login
def beranda(request):
    context ={
        "menu" : 'Beranda',
        "page" : 'Selamat Datang di e-Presensi'
    }
    return render(request, 'akses/beranda.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def formkaryawan(request):
    data = Karyawan.objects.order_by('-id_karyawan')
    context ={
        "menu" : 'Form Karyawan',
        "page" : 'Form Karyawan',
        'karyawan' : data
    }
    return render(request, 'akses/formkaryawan.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def inputkaryawan(request):
    form = KaryawanForm()
    formkarayawan = KaryawanForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada.')
            return redirect('inputkaryawan')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('inputkaryawan')
        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user
        # Group
        akses_karyawan = Group.objects.get(name='karyawan')
        user.groups.add(akses_karyawan)
        # Group
        # Karyawan
        formsimpankaryawan = formkarayawan.save()
        formsimpankaryawan.user = user
        formsimpankaryawan.save()
        # Karyawan
        return redirect('formkaryawan')
    context ={
        "menu" : 'Input Form Karyawan',
        "page" : 'Input Karyawan',
        "form" : form   
    }
    return render(request, 'akses/inputkaryawan.html', context)

@tolakhalaman_ini
def loginPage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')
    context = {
        'menu': 'Halaman Login',
        'page': 'login',
    }
    return render(request, 'akses/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


# Karyawan
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['karyawan'])
def karyawan(request):
    context ={
        "menu" : 'Karyawan',
        "page" : 'Selamat Datang Halaman Karyawan'
    }
    return render(request, 'akses/karyawan/karyawan.html', context)




@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def unit(request):
    pass




