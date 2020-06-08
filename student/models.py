from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from phone_field import PhoneField
from django_countries.fields import CountryField

internshipTypeChocies = (("Akademik", "Akademik"),
                         ("Endüstriyel", "Endüstriyel"))
internshipAbroadOrDomesticChoices = (("Yurt Dışı", "Yurt Dışı"),
                                     ("Yurt İçi", "Yurt İçi"))
numeric = RegexValidator(r'[0-9]', 'Only numeric characters are allowed.')


# Create your models here.
class Student(models.Model):
    tcNum = models.CharField('T.C. Numarası', max_length=11, validators=[MinLengthValidator(11), numeric],
                             primary_key=True)
    studentName = models.CharField('Öğrenci Adı', max_length=60)
    studentSurname = models.CharField('Öğrenci Soyadı', max_length=60)
    studentNum = models.CharField('Öğrenci Numarası', max_length=9, validators=[MinLengthValidator(9), numeric])

    class Meta:
        verbose_name = ("Öğrenci")
        verbose_name_plural = ("Öğrenciler")

    def __str__(self):
        return "%s \t %s \t %s" % (self.studentNum, self.studentName, self.studentSurname)


class InternShip(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    companyName = models.CharField('Firma Adı', max_length=100)
    internshipDuration = models.IntegerField('Staj Süresi')
    startDate = models.DateField('Staj Başlangıç Tarihi')
    finishDate = models.DateField('Staj Bitiş Tarihi')
    catchment = models.CharField('Hizmet Alanı', max_length=60)
    companyPhoneNum = PhoneField('Firma Telefon')
    companyMentorName = models.CharField('Firma İlgili Kişi', max_length=120)
    email = models.EmailField('E-posta Adresi', max_length=120)
    companyAddress = models.TextField('Staj Adresi', max_length=300)
    numberOfEngineers = models.IntegerField('Çalışan Mühendis Sayısı')
    internshipType = models.CharField('Staj Tipi', max_length=20, choices=internshipTypeChocies)
    internshipAbroadOrDomestic = models.CharField('Yurtiçi / Yurtdışı Staj', max_length=20,
                                                  choices=internshipAbroadOrDomesticChoices)
    companyCountry = CountryField('Stajın Yapıldığı Ülke', default='TR')


class InternShipHiddenFields(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.ForeignKey(InternShip,verbose_name='Şirket Adı', on_delete=models.CASCADE)
    internshipDevamNotu = models.IntegerField('Staj Devam Notu')
    internshipCalismaNotu = models.IntegerField('Çalışma Ve Gayret Notu')
    internshipZamanNotu = models.IntegerField('İşi Zamanında ve Tam Yapma Notu')
    internshipAmirNotu = models.IntegerField('Amirine Karşı Tutumu Notu')
    internshipArkadas = models.IntegerField('İşçi ve Arkadaşlarına Karşı Tutumu Notu')
    internshipDiger = models.ImageField('Değerlendirme Formu', upload_to='uploads/')
    firmaDegerlendirme = models.BooleanField('Firma Değerlendirme')
    firmaYorumu = models.TextField('Firma Yorumu')

