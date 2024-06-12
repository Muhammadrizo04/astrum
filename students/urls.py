from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path('', search_certificates, name='search'),
    path('student/MK<str:sertificate_id>/', detail_view_mk, name='detail_view_mk'),
    path('student/3D<str:sertificate_id>/', detail_view_3d, name='detail_view_3d'),
    path('student/FS<str:sertificate_id>/', detail_view_fs, name='detail_view_fs'),
    path('student/SE<str:sertificate_id>/', detail_view_se, name='detail_view_se'),
    path('student/DS<str:sertificate_id>/', detail_view_dt, name='detail_view_ds'),
    path('download/<str:filename>/', download_file, name='download_file'),
    path('student/CS<str:sertificate_id>/', detail_view_cs, name='detail_view_cs'),
    path('student/NA<str:sertificate_id>/', detail_view_na, name='detail_view_na'),
]
