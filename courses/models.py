from django.db import models
from django.core.validators import MinValueValidator


class University(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="UnitedStates")
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
    course_name = models.CharField(max_length=100, null=True)
    gross_tuition_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
    )
    cost_of_living = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
    )
    earliest_intake = models.CharField(max_length=100, null=True)
    program_duration = models.IntegerField(
        choices=PROGRAM_DURATION_CHOICES, default=2, null=True
    )
    program_type = models.CharField(
        max_length=50, choices=PROGRAM_TYPE_CHOICES, null=True
    )
    application_deadline = models.CharField(max_length=100, null=True)
    range_tution_fee = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.course_name} at {self.university}"
