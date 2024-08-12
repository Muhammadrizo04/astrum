from django.shortcuts import get_object_or_404
from .models import *
from django.http import FileResponse
from django.shortcuts import render
from .model import *

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
        elif NetworkAdmin.objects.filter(sertificate_id__iexact=sertificate_id, seria__iexact=seria).exists():
            info = NetworkAdmin.objects.get(sertificate_id__iexact=sertificate_id, seria__iexact=seria)

        if info is not None:
            return render(request, 'sertificate.html', {'info': info})
        else:
            return render(request, 'error.html',
                          {'sertificate_id': sertificate_id, 'seria': seria})
    else:

        return render(request, 'index.html')


def detail_view_mk(request, sertificate_id):
    educator = get_object_or_404(ITEducator, sertificate_id=sertificate_id)
    return render(request, 'info_mk.html', {'educator': educator})


def detail_view_3d(request, sertificate_id):
    student_3d = get_object_or_404(InteriorDesign, sertificate_id=sertificate_id)
    return render(request, 'info_3d.html', {'student_3d': student_3d})


def detail_view_fs(request, certificate_id):
    student_fs = get_object_or_404(FullStack, certificate_id=certificate_id, series='FS')
    return render(request, 'info_fs.html', {'student_fs': student_fs})


def detail_view_fd(request, certificate_id):
    student_fd = get_object_or_404(FullStack, certificate_id=certificate_id, series='FD')
    return render(request, 'info_fd.html', {'student_fd': student_fd})


def detail_view_bd(request, certificate_id):
    student_bd = get_object_or_404(FullStack, certificate_id=certificate_id, series='BD')
    return render(request, 'info_bd.html', {'student_bd': student_bd})


def detail_view_se(request, sertificate_id):
    student_se = get_object_or_404(SoftWare, sertificate_id=sertificate_id)
    return render(request, 'info_se.html', {'student_se': student_se})


def detail_view_dt(request, sertificate_id):
    student_dt = get_object_or_404(DataSciense, sertificate_id=sertificate_id)
    return render(request, 'info_dt.html', {'student_dt': student_dt})


def detail_view_cs(request, sertificate_id):
    student_cs = get_object_or_404(CyberSecurity, sertificate_id=sertificate_id)
    return render(request, 'info_cs.html', {'student_cs': student_cs})


def detail_view_na(request, sertificate_id):
    student_na = get_object_or_404(NetworkAdmin, sertificate_id=sertificate_id)
    return render(request, 'info_na.html', {'student_na': student_na})


def detail_view_other(request, seria, sertificate_id):
    student_other = get_object_or_404(Other, seria=seria, sertificate_id=sertificate_id)
    return render(request, 'info_other.html', {'student_other': student_other})
