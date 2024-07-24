
from email.policy import default
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import User
from pickle import TRUE
# Create your models here.

class register(models.Model):
    username= models.CharField(max_length=20)
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    email= models.EmailField( max_length=30)
    dob= models.DateField()
    password= models.CharField(max_length=10)
    UniqueConstraint(fields = ['username', 'email'], name = 'primarykey')  #combination of primary 
    def __str__(self):
        return self.email
    

class detail(models.Model):
    pid=models.CharField(max_length=10,primary_key=True)
    pname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics')
    price= models.FloatField(max_length=30)
    manufdate=models.DateField(null=True)
    expirydate=models.DateField(null=True)
    def __str__(self):
        return self.pid
    

class order(models.Model):
    fullname=models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.BigIntegerField()
    address=models.TextField()
    Orderno=models.IntegerField(primary_key=True)
    Orderdate=models.DateTimeField(auto_now_add=True,null=True)
    deliverydate=models.DateTimeField(auto_now_add=True,null=True)

class payment(models.Model):
    payid=models.IntegerField(default='null')
    mode=models.CharField(max_length=30, default="Cash on delivery")
    price=models.FloatField()
    email=models.ForeignKey(register,on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    qno=models.IntegerField
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

class Userans(models.Model):
    username=models.CharField(max_length=200)
    qans1=models.CharField(max_length=200)
    qans2=models.CharField(max_length=200)
    qans3=models.CharField(max_length=200)
    qans4=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.username

class Options(models.Model):
    pid=models.ForeignKey(detail,on_delete=models.CASCADE)
    qans1=models.CharField(max_length=200)
    qans2=models.CharField(max_length=200)
    qans3=models.CharField(max_length=200)
    qans4=models.CharField(max_length=200,null=True)
    def ___str__(self):
        return self.pid

    