from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Unit(models.Model):
    id_unit = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fakultas = models.CharField(max_length=200, blank=True, null=True)
    nama_dekan =  models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fakultas
    class Meta:
        verbose_name_plural ="Unit"

class Karyawan(models.Model):
    Pilihan=(
        ('pimpinan', 'pimpinan'),
        ('karyawan' , 'karyawan'),
    )
    id_karyawan = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    id_unit = models.ForeignKey(Unit, blank=True, null= True, on_delete=models.SET_NULL)
    nama_karyawan = models.CharField(max_length=200)
    telp_karyawan =  models.CharField(max_length=100)
    status = models.CharField(max_length=150, blank=True, null=True, choices=Pilihan)

    def __str__(self):
        return '%s' % (self.nama_karyawan)
    class Meta:
        verbose_name_plural ="Karyawan"