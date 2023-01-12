from django.db import models

class Angajati(models.Model):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    firma = models.CharField(max_length=100)
    link = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name} -> {self.country} -> {self.firma} -> {self.link}"


class Log(models.Model):
    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)