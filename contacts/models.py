from django.db import models


class State(models.Model):
    state = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return str(self.state)


class City(models.Model):
    state = models.ForeignKey(State)
    city = models.CharField(max_length=48)

    def __str__(self):
        return str(self.city)


class Contact(models.Model):
    user = models.CharField(max_length=24, unique=True)    
    first_name = models.CharField(max_length=24, blank=True, null=True)
    last_name = models.CharField(max_length=24, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=96, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)

    def __str__(self):
        return str(self.first_name)

