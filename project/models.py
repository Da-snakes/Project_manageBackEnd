from django.db import models

# Create your models here.
from django.db import models

choice = (
    ('1','NEW'), ('2', 'OPEN'), ('3','RESOLVED'), ('4','COLSED'),('5','IN PROGRESS'),
)

class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    position = models.OneToOneField(Position, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name+'  '+self.last_name

class Project (models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Task(models.Model):
    name = models.CharField(max_length=30)
    status = models.CharField(choices=choice,default='1',max_length=333)
    description = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    dead_line = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Widget(models.Model):
    name = models.CharField(max_length=30)
    tache = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




