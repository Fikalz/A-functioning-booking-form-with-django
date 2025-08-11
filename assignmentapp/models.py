from django.db import models

# Create your models here.
# from django.db import models

class Booking(models.Model):
    PERSON_CHOICES = [
        ('1', 'Person 1'),
        ('2', 'Person 2'),
        ('3', 'Person 3'),
        ('4', 'Person 4'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    person = models.CharField(max_length=1, choices=PERSON_CHOICES)

    def __str__(self):
        return f"Booking by {self.name} on {self.date} at {self.time}"
