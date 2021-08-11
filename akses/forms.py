from django import forms
from django.forms import ModelForm
from .models import Karyawan
class KaryawanForm(ModelForm):
    class Meta:
        model = Karyawan
        fields= ['id_unit','nama_karyawan','telp_karyawan','status']

        widgets = {
            'id_unit': forms.Select(attrs={'class': 'form-select'}),
            'nama_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'telp_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'id_unit': 'Fakultas',
            'nama_karyawan': 'Nama Karyawan',
            'telp_karyawan': 'Telp Karyawan',
        }

        

