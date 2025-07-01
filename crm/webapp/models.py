from django.db import models

# Customer Table

class Customer(models.Model):
    Id = models.AutoField(primary_key=True)
    Creation_date = models.DateTimeField(auto_now_add=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True)
    Phone = models.CharField(max_length=15, unique=True)
    Address = models.TextField()
    City = models.CharField(max_length=50)
    Province = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.FirstName + " " + self.LastName
