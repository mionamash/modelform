from django.shortcuts import render
from modelapp.forms import StudentsForm

def home(request):
    stud=StudentsForm
    return render(request,'index.html',{'form':stud})
