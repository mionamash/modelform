from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
    contacts = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'student'
