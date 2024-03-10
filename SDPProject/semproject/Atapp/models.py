from django.db import models

# Create your models here.


class Book(models.Model):
    firstname=models.CharField(max_length=25,blank=False)
    lastname=models.CharField(max_length=25,blank=False)
    email=models.EmailField(max_length=25,blank=False,unique=True)
    phone=models.BigIntegerField(blank=False,unique=True)
    gender_choices = (("M", "Male"), ("F", "Female"), ("Others", "Prefer not to say"))
    gender = models.CharField(blank=False, choices=gender_choices, max_length=10)
    age=models.BigIntegerField(blank=False,unique=True)
    pincode=models.BigIntegerField(blank=False)
    state=models.CharField(max_length=25,blank=False)
    description=models.TextField()

    class Meta:
        db_table = "book_table"


class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    class Meta:
        db_table = "contact_table"


class News(models.Model):
    email=models.EmailField()

    class Meta:
        db_table = "news_table"