from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name    

# option field
sex_choices = (
   ('f', 'female'),
   ('m', 'male')
)
class User(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices=sex_choices)
    
    def __str__(self):
        return self.name

# one to many class
class Entry(models.Model):
    name = models.CharField(max_length=30)

class Blog(models.Model):
    name = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry)

# many to many class
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name