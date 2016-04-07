from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class student(models.Model):
#     firstname=models.CharField(max_length=20)
#     lastname=models.CharField(max_length=20)
#     username=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)
#     email=models.CharField(max_length=20)
#     mobile=models.IntegerField()
#     
# class company(models.Model):
#     cname=models.CharField(max_length=30)
#     username=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)
#     email=models.CharField(max_length=20)
#     mobile=models.IntegerField()    
    
class contact(models.Model):
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=20)
    mobile=models.IntegerField(null=True)
    temporary_address=models.CharField(max_length=20)
    permanent_address=models.CharField(max_length=20,null=True)
    website=models.CharField(max_length=20)
   
class internships(models.Model):
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=20)
    field1=models.CharField(max_length=200,null=True)
    field2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200,null=True)
    
class postgrad(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    Last_spi=models.FloatField(max_length=10)
    Cpi=models.FloatField(max_length=10)
    Branch_of_study=models.CharField(max_length=20)

class undergrad(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    Last_spi=models.FloatField(max_length=10)
    Cpi=models.FloatField(max_length=10)
    Branch_of_study=models.CharField(max_length=20)

class srsec(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    percentage_obtained=models.FloatField(max_length=10)
    school=models.CharField(max_length=10)
    Board=models.CharField(max_length=20)
    
class sec(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    percentage_or_cpi=models.FloatField(max_length=10)
    school=models.CharField(max_length=10)
    Board=models.CharField(max_length=20)
    
class languages(models.Model):
    username=models.CharField(max_length=20)
    languages_known=models.CharField(max_length=40)   
    
class projects(models.Model):
    username=models.CharField(max_length=20)
    title=models.CharField(max_length=40)
    position=models.CharField(max_length=40)
    duration=models.CharField(max_length=40)
    description=models.CharField(max_length=200)
    projects_related_url=models.CharField(max_length=50)
    
class photo(models.Model):
    username=models.CharField(max_length=20)
    links=models.CharField(max_length=50)