from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import StudentRegistration
from .models import User
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



@login_required
def addShow(request):
 
    # check if the request is post
    if request.method =='POST': 
        form = StudentRegistration(request.POST)
        if form.is_valid(): 
 
            post = form.save(commit = False)
 
            post.save() 
             
        else:
            pass

            #return render(request, "enroll/addandshow.html", {'form':form}) 
    else:
 
        form = StudentRegistration(None)  
        #return render(request, 'enroll/addandshow.html', {'form':form})
    stud = User.objects.all()
    p = Paginator(stud, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'addandshow.html', {'form': form, 'stu': page})

@login_required

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

    return render(request, 'updatestudent.html',{'form':fm})


def Register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            return HttpResponseRedirect('login')
        else:
            print('form is invalid')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form':form})
