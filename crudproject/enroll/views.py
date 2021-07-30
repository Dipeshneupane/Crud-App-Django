from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.core.paginator import Paginator, EmptyPage

def addShow(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    p = Paginator(stud, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': page})



# Create your views here.

def deleteData(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')

def updateData(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance = pi)

    return render(request, 'enroll/updatestudent.html',{'form':fm})