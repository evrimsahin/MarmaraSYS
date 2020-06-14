from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import xlwt
from django.http import HttpResponse
from student.models import Student


def loginPage(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('index')
    elif request.user.is_authenticated and request.user.is_staff:
        logout(request)
        return redirect('')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and not user.is_staff:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def registerPage(request):
    context = {}
    return render(request, 'accounts/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def indexPage(request):
    if not request.user.is_staff:
        context = {}
        return render(request, 'accounts/index.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Parola Başarılı Bir Şekilde Güncellendi')
            logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Hatalı Yeni Şifre Denemesi')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html')


@login_required(login_url='admin')
def export_users_xls_2018_2019(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students_2018_2019.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Students')


    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Numara','Ad', 'Soyad', 'TC No','Şirket Adı','Başlangıç Tarihi','Bitiş Tarihi','Staj Süresi','Hizmet Alanı','Firma İlgili Kişi','Firma E-Posta','Şirket Adresi','Çalışan Mühendis Sayısı','Staj Tipi','Yurtiçi / YurtDışı Staj']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)


    font_style = xlwt.XFStyle()

    rows = Student.objects.filter(internship__startDate__range=["2018-01-01", "2019-01-01"]).all().values_list('studentNum','studentName','studentSurname','tcNum','internship__companyName','internship__startDate','internship__finishDate','internship__internshipDuration',
                                                                                                               'internship__catchment','internship__companyMentorName','internship__email','internship__companyAddress','internship__numberOfEngineers',
                                                                                                               'internship__internshipType','internship__companyCountry','internship__internshipAbroadOrDomestic')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url='admin')
def export_users_xls_2019(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students_2019.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Students')


    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Numara','Ad', 'Soyad', 'TC No','Şirket Adı','Başlangıç Tarihi','Bitiş Tarihi','Staj Süresi','Hizmet Alanı','Firma İlgili Kişi','Firma E-Posta','Şirket Adresi','Çalışan Mühendis Sayısı','Staj Tipi','Yurtiçi / YurtDışı Staj']


    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)


    font_style = xlwt.XFStyle()

    rows = Student.objects.filter(internship__startDate__range=["2019-01-01", "2020-01-01"]).all().values_list('studentNum','studentName','studentSurname','tcNum','internship__companyName','internship__startDate','internship__finishDate','internship__internshipDuration',
                                                                                                               'internship__catchment','internship__companyMentorName','internship__email','internship__companyAddress','internship__numberOfEngineers',
                                                                                                               'internship__internshipType','internship__companyCountry','internship__internshipAbroadOrDomestic')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response