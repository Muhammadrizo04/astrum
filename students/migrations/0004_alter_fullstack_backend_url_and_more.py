# Generated by Django 4.2.7 on 2023-11-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_datasciense_sertificate_id_numeric_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullstack',
            name='backend_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fullstack',
            name='frontend_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='rust_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
