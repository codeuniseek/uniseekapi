from rest_framework import serializers
from .models import Course, University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ["name", "website", "address", "popular_courses", "about"]


class CourseSerializer(serializers.ModelSerializer):
    university = (
        UniversitySerializer()
    )  # Embed UniversitySerializer inside CourseSerializer

    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        university_data = representation.pop("university")
        for key, value in university_data.items():
            representation[key] = value
        return representation
