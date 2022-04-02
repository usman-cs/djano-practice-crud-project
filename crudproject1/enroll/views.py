from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    data = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stud':data})

def delete_data(request,id):
    d = User.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        d = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=d)
        if fm.is_valid():
            fm.save()
    else:
        d = User.objects.get(pk=id)
        fm = StudentRegistration(instance = d)
    return render(request,'enroll/updatestudent.html',{'form':fm})