from django.db import models

# Create your models here.


class Profile(models.Model):
    slackUsername = models.CharField(max_length=20, unique=True)
    backend = models.BooleanField()
    age = models.PositiveIntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername