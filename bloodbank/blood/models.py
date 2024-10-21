from django.db import models

# Create your models here.

class BloodType(models.Model):
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.blood_group

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    last_donation = models.DateField()

    def __str__(self):
        return self.name

class BloodBank(models.Model):
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    quantity_in_units = models.IntegerField()

    def __str__(self):
        return f"{self.blood_type} - {self.quantity_in_units} units"

class Request(models.Model):
    recipient_name = models.CharField(max_length=100)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    quantity_needed = models.IntegerField()
    request_date = models.DateField()

    def __str__(self):
        return self.recipient_name
