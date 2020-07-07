from django.db import models

# Create your models here.
class Hospital(models.Model):
    hopsital_id = models.IntegerField(default=0)
    hospital_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.hospital_name

class Service(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.service_name
