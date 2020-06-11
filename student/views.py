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
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_staff is not None:
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
    context = {}
    return render(request, 'accounts/index.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:


            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html')


@login_required(login_url='admin')
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Students')


    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Ad', 'Soyad', 'TC No','Şirket Adı','Başlangıç Tarihi','Bitiş Tarihi']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)


    font_style = xlwt.XFStyle()

    rows = Student.objects.filter(internship__startDate__range=["2019-01-01", "2020-01-31"]).all().values_list('studentNum','studentName','tcNum','internship__companyName','internship__startDate','internship__finishDate')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response