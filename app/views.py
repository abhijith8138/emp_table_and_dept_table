from django.shortcuts import render
from app.models import *

# Create your views here.
def display_dept(request):
    LOD=Dept.objects.all()
    d={'dept': LOD}
    return render(request,'display_dept.html',context=d)
def display_emp(request):
    LOE=Emp.objects.all()
    d={'emp': LOE}
    return render(request,'display_emp.html',context=d)
