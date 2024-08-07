# Generated by Django 4.2.7 on 2024-06-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_cybersecurity_sharif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iteducator',
            old_name='sertificate_back',
            new_name='certificate_back',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='sertificate_front',
            new_name='certificate_front',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='sertificate_id',
            new_name='certificate_id',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='sertificate_id_numeric',
            new_name='certificate_id_numeric',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='berilgan_vaqt',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='familya',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='amal_qilish',
            new_name='issue_date',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='ism',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='sharif',
            new_name='middle_name',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='modul_1_ball',
            new_name='module_1_percentage',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='modul_1p',
            new_name='module_1_score',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='modul_2_ball',
            new_name='module_2_percentage',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='modul_2p',
            new_name='module_2_score',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='modul_3_ball',
            new_name='module_3_percentage',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='modul_3p',
            new_name='module_3_score',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='umumiy_ball',
            new_name='overall_percentage',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='umumiy_p',
            new_name='overall_score',
        ),
        migrations.RenameField(
            model_name='iteducator',
            old_name='seria',
            new_name='series',
        ),
    ]
