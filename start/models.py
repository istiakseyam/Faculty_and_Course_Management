from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Day(models.Model):
    day= models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.day


class Time(models.Model):
    time= models.CharField(max_length=5, blank=False, null=False, unique=True)

    def __str__(self):
        return self.time

class Course(models.Model):
    cname=models.CharField(max_length=10, unique=True)#unique section
    crd=models.IntegerField(blank=False, null=False)
    cday=models.ForeignKey(Day,to_field='day', on_delete=models.CASCADE)
    ctime=models.ForeignKey(Time,to_field='time', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname
    class Meta:
        unique_together = (("cday", "ctime","cname"),)#each section time is unique, no clash

class Faculty(models.Model):
    fmane=models.CharField(max_length=30)
    initial=models.CharField(max_length=5,unique=True)
    crd_limit=models.IntegerField()

    def __str__(self):
        return self.initial

class Takes(models.Model):
    fac=models.ForeignKey(Faculty,to_field='initial', on_delete=models.CASCADE)
    cour=models.ForeignKey(Course,to_field='cname', on_delete=models.CASCADE)

    def save(self):
        #geting another model
        faculty = Faculty.objects.get(initial=self.fac)
        f_crd=faculty.crd_limit
        course=Course.objects.get(cname=self.cour)
        cour_crd=course.crd
        rest=f_crd-cour_crd
        if(rest>=0):
            faculty.crd_limit=rest
            #another model save
            faculty.save()
            #this model save
            super().save()
        else:
            raise ValidationError("Cannot save the entity due to invalid condition")
            
    class Meta:
        unique_together = (("fac", "cour"),) 
        #we can't give same course to another faculty for this combition  
    