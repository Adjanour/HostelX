from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Test(models.Model):
    test_date = models.DateField()
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default =False)

    def __str__(self):
        return self.description