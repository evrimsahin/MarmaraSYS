from django.shortcuts import render

def loginview(request):
    return render(request,'index.html',{})
