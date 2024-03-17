from django.db import models
from django.core.validators import MinValueValidator


class Course(models.Model):
    PROGRAM_TYPE_CHOICES = [
        ("Bachelors Degree", "Bachelors Degree"),
        ("Masters Degree", "Masters Degree"),
    ]

    PROGRAM_DURATION_CHOICES = [
        (2, "2 Years"),
        (3, "3 Years"),
        (4, "4 Years"),
    ]

    university_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    gross_tuition_fee = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0
    )
    cost_of_living = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0
    )
    earliest_intake = models.CharField(max_length=20)
    program_duration = models.IntegerField(choices=PROGRAM_DURATION_CHOICES, default=0)
    program_type = models.CharField(max_length=50, choices=PROGRAM_TYPE_CHOICES)
    state = models.CharField(max_length=50)
    application_deadline = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name} at {self.university_name}"
