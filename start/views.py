from django.shortcuts import render
from .models import Day, Time, Course, Faculty, Takes

# Create your views here.

def home(req):
    allFac= Faculty.objects.all()
    allcourse=Course.objects.all()
    fac=Faculty.objects.all()[:10]
    course=Course.objects.all()[:10]
    return render(req, "start/includes/home.html",{
        'allFac': allFac,
        'allCourse': allcourse,
        'fac': fac,
        'course': course
        })
def all_fac(req):
    allFac= Faculty.objects.all()
    return render(req, "start/includes/all_fac.html",{
        'allFac': allFac,
        })
def all_cour(req):
    allFac= Course.objects.all()
    return render(req, "start/includes/all_cour.html",{
        'allCour': allFac,
        })

def fac_view(req, a, **args):
    print(type(a))
    fac=Faculty.objects.get(initial=a)
    takes=Takes.objects.filter(fac= a)
    #takes=Takes.objects.get(fac=a)
    courses=[]
    print(fac.fmane)
    for c in takes:
        course=Course.objects.get(cname=c.cour)
        courses.append(course)
    #print(takes[0])
    return render(req, "start/includes/fac_view.html",{
        'fac': fac,
        'takes': takes,
        'cour': courses
    })