from django.db import models

# Create your models here.

class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)

    def __str__(self):
        return self.stuname
    
class Teacher(models.Model):
    teacherid = models.IntegerField()
    teachername = models.CharField(max_length=70)
    teacheremail = models.EmailField(max_length=70)
    teacherpass = models.CharField(max_length=70)

    def __str__(self):
        return str(self.teacherid)
    