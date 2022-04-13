from django.db import models
import os

def rename(instance, filename):
    directory = 'pegawai'
    ext = filename.split('.')[-1]
    filename = f'{instance.nama}.{ext}'
    return os.path.join(directory, filename)
class Shift(models.Model):
    id_shift = models.BigAutoField(primary_key=True)
    masuk = models.TimeField()
    pulang = models.TimeField()

class Jabatan(models.Model):
    nama_jabatan = models.CharField(max_length=100)

class Pegawai(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    nohp = models.CharField(max_length=12)
    alamat = models.TextField(blank=True)
    foto = models.ImageField(upload_to=rename, blank=True)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nama}'

class Presensi(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=255)
    tanggal = models.DateField()
    check_in = models.TimeField()
    late_in = models.CharField(max_length=3)
    check_out = models.TimeField()
    ket = models.CharField(max_length=100)
    suhu = models.CharField(max_length=5)