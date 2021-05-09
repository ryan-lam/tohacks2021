from django.db import models

# Create your models here.

class Profile(models.Model):
    GENDERS = (
        ('M', 'M'),
        ('F', 'F'),
        ('Other', 'Other'),
    )
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.CharField(max_length=64)
    gender = models.CharField(max_length=64, choices=GENDERS)



class Client(Profile):
    income = models.IntegerField()
    def __str__(self):
        return f"Client: {self.username} : {self.name} : {self.age} : {self.address} : {self.gender} : {self.income}"


class Rep(Profile):
    EXPERTISES = (
        ('AUTO','AUTO'),
        ('HOME', 'HOME'),
    )

    expertise = models.CharField(max_length=256, choices=EXPERTISES)
    description = models.CharField(max_length=500)
    hours = models.CharField(max_length=256)

    def __str__(self):
        return f"Rep: {self.username} : {self.name} : {self.age} : {self.address} : {self.gender} : {self.expertise} : {self.description} : {self.hours}"


class Appointments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client", null=True)
    rep = models.ForeignKey(Rep, on_delete=models.CASCADE, related_name="rep", null=True)
    time = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.client} : {self.rep} : {self.time}"