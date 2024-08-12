from django.db import models


class Other(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    sharif = models.CharField(max_length=50)
    berilgan_vaqt = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    seria = models.CharField(max_length=3)
    sertificate_id = models.CharField(max_length=6, unique=True, blank=True)
    sertificate_id_numeric = models.IntegerField(unique=True, blank=True)
    pptx_file = models.FileField(upload_to='pptx_other', blank=True)
    sertificate_front = models.FileField(upload_to='other_ser_front/', blank=True)

    def __str__(self):
        return self.ism
