# Generated by Django 4.2.7 on 2024-08-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_cybersecurity_amal_qilish_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkadmin',
            name='create_date',
        ),
        migrations.AddField(
            model_name='networkadmin',
            name='amal_qilish',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkadmin',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='ccna_qrcode/'),
        ),
        migrations.AlterField(
            model_name='networkadmin',
            name='berilgan_vaqt',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='networkadmin',
            name='seria',
            field=models.CharField(default='NA', max_length=3),
        ),
    ]
