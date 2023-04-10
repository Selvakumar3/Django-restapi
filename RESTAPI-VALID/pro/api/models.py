from django.db import models


class Students(models.Model):  # ---- parent class ----
    
    Admin_id = models.IntegerField(primary_key=True)
    College = models.CharField(max_length=100)
    
    def __str__(self):
        return self.College

class Details(models.Model):  # ----- child classes
    
    Stuid =models.IntegerField(primary_key=True)
    Name =models.CharField(max_length=50)
    Age=models.DateField()
    Gender=models.CharField(max_length=50)
    Degree=models.TextField(max_length=50)
    Email = models.EmailField()
    Address=models.TextField(max_length=255)
    image=models.ImageField(upload_to='picture/%Y/%m/%d', blank=True)
    Admin_id = models.ForeignKey(Students,related_name='Details',on_delete=models.CASCADE)
