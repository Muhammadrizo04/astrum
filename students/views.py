import mimetypes

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from django.http import HttpResponse, FileResponse
import csv
from io import TextIOWrapper
from datetime import datetime
from django.shortcuts import render
from io import BytesIO
from .forms import SearchForm


def search_certificates(request):
    if 'sertificate_id' in request.GET and 'seria' in request.GET:
        sertificate_id = request.GET['sertificate_id']
        seria = request.GET['seria']

        info = None  # Bo'sh ma'lumotlarni aniqlash uchun o'zgaruvchi

        # Ma'lumotlarni 4 ta model orasida qidirish
        if ITEducator.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = ITEducator.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)
        elif InteriorDesign.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = InteriorDesign.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)
        elif FullStack.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = FullStack.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)
        elif DataSciense.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = DataSciense.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)
        elif SoftWare.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = SoftWare.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)
        elif Other.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = Other.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)

        if info is not None:
            return render(request, 'index.html', {'info': info})
        else:
            error_message = 'Berilgan ID raqamiga ega talaba topilmadi'
            return render(request, 'index.html',
                          {'error_message': error_message, 'sertificate_id': sertificate_id, 'seria': seria})
    else:
        error_message = 'Qidiruv uchun sertifikat ID raqamini va seria ni taqdim eting'
        return render(request, 'index.html', {'error_message': error_message})


def detail_view_mk(request, sertificate_id):
    educator = get_object_or_404(ITEducator, sertificate_id=sertificate_id)
    return render(request, 'info_mk.html', {'educator': educator})


def detail_view_3d(request, sertificate_id):
    student = get_object_or_404(InteriorDesign, sertificate_id=sertificate_id)
    return render(request, 'info_mk.html', {'student': student})


def detail_view_fs(request, sertificate_id):
    student = get_object_or_404(FullStack, sertificate_id=sertificate_id)
    return render(request, 'info_fs.html', {'student': student})


def detail_view_se(request, sertificate_id):
    student = get_object_or_404(SoftWare, sertificate_id=sertificate_id)
    return render(request, 'info_se.html', {'student': student})


def detail_view_dt(request, sertificate_id):
    student = get_object_or_404(DataSciense, sertificate_id=sertificate_id)
    return render(request, 'info_dt.html', {'student': student})

def detail_view_cs(request, sertificate_id):
    student = get_object_or_404(Other, sertificate_id=sertificate_id)
    return render(request, 'info_cs.html', {'student': student})


def download_file(request, filename):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filepath = os.path.join(BASE_DIR, 'static', 'test', filename)

    # Set the return value of the FileResponse
    response = FileResponse(open(filepath, 'rb'))
    # Set the mime type
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    # Set the HTTP header for sending to the browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
