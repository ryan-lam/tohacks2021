from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)


    def __str__(self):
        return f"Client: {self.username} : {self.name} : {self.age} : {self.address} : {self.gender}"

class Client(Profile):
    income = models.IntegerField()


class Rep(Profile):
    expertise = models.CharField(max_length=256)
    division = models.CharField(max_length=256)
    hours = models.CharField(max_length=256)

    def __str__(self):
        return f"Rep: {self.username} : {self.name} : {self.age} : {self.address} : {self.gender} : {self.expertise} : {self.division} : {self.hours}"


class Appointments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client", null=True)
    rep = models.ForeignKey(Rep, on_delete=models.CASCADE, related_name="rep", null=True)
    time = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.client} : {self.rep} : {self.time}"