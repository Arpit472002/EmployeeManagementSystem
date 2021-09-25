from django.db import models

# Create your models here.
class EmployeeList(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    salary=models.IntegerField()
    date_of_joining=models.DateField()
    today=models.DateField(auto_now_add=True)
    picture=models.ImageField(upload_to='images/',default='images/default.jpg')
    def __str__(self):
        return self.name