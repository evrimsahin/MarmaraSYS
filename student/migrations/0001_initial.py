# Generated by Django 3.0.5 on 2020-04-09 13:19

import django.core.validators
from django.db import migrations, models
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('tcNum', models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.RegexValidator('[0-9]', 'Only numeric characters are allowed.')], verbose_name='T.C. Numarası')),
                ('studentName', models.CharField(max_length=60, verbose_name='Öğrenci Adı')),
                ('studentSurname', models.CharField(max_length=60, verbose_name='Öğrenci Soyadı')),
                ('studentNum', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.RegexValidator('[0-9]', 'Only numeric characters are allowed.')], verbose_name='Öğrenci Numarası')),
                ('companyName', models.CharField(max_length=100, verbose_name='Firma Adı')),
                ('internshipDuration', models.IntegerField(verbose_name='Staj Süresi')),
                ('startDate', models.DateField(verbose_name='Staj Başlangıç Tarihi')),
                ('finishDate', models.DateField(verbose_name='Staj Bitiş Tarihi')),
                ('catchment', models.CharField(max_length=60, verbose_name='Hizmet Alanı')),
                ('companyPhoneNum', phone_field.models.PhoneField(max_length=31, verbose_name='Firma Telefon')),
                ('companyMentorName', models.CharField(max_length=120, verbose_name='Firma İlgili Kişi')),
                ('email', models.EmailField(max_length=120, verbose_name='E-posta Adresi')),
                ('companyAddress', models.TextField(max_length=300, verbose_name='Staj Adresi')),
                ('numberOfEngineers', models.IntegerField(verbose_name='Çalışan Mühendis Sayısı')),
                ('internshipType', models.CharField(choices=[('Akademik', 'Akademik'), ('Endüstriyel', 'Endüstriyel')], max_length=20, verbose_name='Staj Tipi')),
                ('internshipAbroadOrDomestic', models.CharField(choices=[('Yurt Dışı', 'Yurt Dışı'), ('Yurt İçi', 'Yurt İçi')], max_length=20, verbose_name='Yurtiçi / Yurtdışı Staj')),
                ('companyCountry', django_countries.fields.CountryField(default='TR', max_length=2, verbose_name='Stajın Yapıldığı Ülke')),
            ],
        ),
    ]
