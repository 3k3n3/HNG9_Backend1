from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

# Task1
class Profile(models.Model):
    slackUsername = models.CharField(max_length=20, unique=True)
    backend = models.BooleanField()
    age = models.PositiveIntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername

# Task2
class Operation(models.Model):

    class Arithmetic(models.TextChoices):
        AD = 'addition', _('Addition')
        SB = 'subtraction', _('Subtraction')
        MP = 'multiplication', _('Multiplication')

    slackUsername = models.CharField(max_length=20, default='maestro')
    result = models.IntegerField(null=True, blank=True)
    # operation_type = models.CharField(max_length=255, choices=Arithmetic.choices)
    operation_type = models.CharField(max_length=255)
    x = models.IntegerField()
    y = models.IntegerField()

    def save(self, *args, **kwargs):

        ADDITION = ['addition', 'add', 'sum', 'summation','plus']
        SUBRACTION = ['difference', 'subtraction', 'reduce', 'decrease', 'minus']
        MULTIPLICATION = ['times', 'multiply', 'product', 'multiplication']

        wordList = [x.lower() for x in self.operation_type.split(' ')]

        for x in wordList:
            if x in ADDITION:
                self.result = self.x + self.y

            elif x in SUBRACTION:
                self.result = self.x - self.y

            elif x in MULTIPLICATION:
                self.result = self.x * self.y

        super().save(*args, **kwargs)


    # # using enum/choicefield
    # def save(self, *args, **kwargs):
    #     if self.operation_type == 'addition':
    #         self.result = self.x + self.y
    #     elif self.operation_type == 'subtraction':
    #         self.result = self.x - self.y
    #     elif self.operation_type == 'multiplication':
    #         self.result = self.x * self.y
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.slackUsername
