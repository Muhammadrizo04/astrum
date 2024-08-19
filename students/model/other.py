from django.db import models


class Other(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    issue_date = models.CharField(max_length=200)
    expiration_date = models.CharField(max_length=100, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    series = models.CharField(max_length=3)
    certificate_id = models.CharField(max_length=6, unique=True, blank=True)
    certificate_id_numeric = models.IntegerField(unique=True, blank=True)
    pptx_file = models.FileField(upload_to='pptx_other', blank=True)
    certificate_front = models.FileField(upload_to='other_ser_front/', blank=True)

    def __str__(self):
        return self.first_name
