from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phone_field import PhoneField
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

internshipTypeChocies = (("Akademik", "Akademik"),
                         ("Endüstriyel", "Endüstriyel"))
internshipAbroadOrDomesticChoices = (("Yurt Dışı", "Yurt Dışı"),
                                     ("Yurt İçi", "Yurt İçi"))
firmaDegerlendirme = (("Olumlu", "Olumlu"),
                     ("Olumsuz", "Olumsuz"))
numeric = RegexValidator(r'[0-9]', 'Only numeric characters are allowed.')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tcNum = models.CharField('T.C. Numarası', max_length=11, validators=[MinLengthValidator(11), numeric])
    studentName = models.CharField('Öğrenci Adı', max_length=60)
    studentSurname = models.CharField('Öğrenci Soyadı', max_length=60)
    studentNum = models.CharField('Öğrenci Numarası', max_length=9, validators=[MinLengthValidator(9), numeric])

    class Meta:
        verbose_name = ("Kullanıcı")
        verbose_name_plural = ("Kullanıcılar")

    def __str__(self):
        return "%s \t %s \t %s" % (self.studentNum, self.studentName, self.user.username)


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

    class Meta:
        verbose_name = ("Staj")
        verbose_name_plural = ("Stajlar")

    def __str__(self):
        return "%s" % (self.companyName)


class InternShipHiddenFields(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.OneToOneField(InternShip, verbose_name='Şirket Adı', on_delete=models.CASCADE)
    internshipDevamNotu = models.IntegerField('Staj Devam Notu')
    internshipCalismaNotu = models.IntegerField('Çalışma Ve Gayret Notu')
    internshipZamanNotu = models.IntegerField('İşi Zamanında ve Tam Yapma Notu')
    internshipAmirNotu = models.IntegerField('Amirine Karşı Tutumu Notu')
    internshipArkadas = models.IntegerField('İşçi ve Arkadaşlarına Karşı Tutumu Notu')
    internshipDiger = models.ImageField('Değerlendirme Formu', upload_to='uploads/')
    firmaDegerlendirme = models.CharField('Firma Değerlendirme',choices=firmaDegerlendirme,max_length=20)
    firmaYorumu = models.TextField('Firma Yorumu')

    class Meta:
        verbose_name = ("Staj Bilgileri(Gizli İçerik)")

    def __str__(self):
        return "%s" % (self.internship.companyName)
