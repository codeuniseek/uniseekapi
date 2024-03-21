from django.db import models
from django.core.validators import MinValueValidator


class University(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=200)
    popular_courses = models.TextField()
    address = models.CharField(max_length=200)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name


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

    university = models.ForeignKey(
        University, on_delete=models.CASCADE, related_name="courses"
    )
    course_name = models.CharField(max_length=100)
    gross_tuition_fee = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0
    )
    cost_of_living = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0
    )
    earliest_intake = models.CharField(max_length=100)
    program_duration = models.IntegerField(choices=PROGRAM_DURATION_CHOICES, default=2)
    program_type = models.CharField(max_length=50, choices=PROGRAM_TYPE_CHOICES)
    application_deadline = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name} at {self.university}"
