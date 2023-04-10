from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=200)
    loc=models.CharField(max_length=200)
    def __str__(self):
        return self.Dname
class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=200)
    Job=models.CharField(max_length=200)
    Mgr=models.IntegerField(null=True)
    Hiredate=models.DateField(null=True)
    Sal=models.IntegerField()
    Comm=models.IntegerField(null=True)
    Dept_no=models.ForeignKey(Dept,on_delete= models.CASCADE)
    

