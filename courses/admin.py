from django.contrib import admin
from courses.models import Course, University
from import_export.admin import ImportExportModelAdmin

# from .utils import import_courses_from_csv


class CourseAdmin(ImportExportModelAdmin):
    list_display = [
        "university",
        "course_name",
        "gross_tuition_fee",
        "earliest_intake",
        "program_duration",
        "program_type",
        "application_deadline",
        "range_tution_fee",
    ]
    list_filter = [
        "university",
        "program_type",
        "earliest_intake",
        "course_name",
    ]


class UniversityAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
        "website",
        "popular_courses",
        "address",
        "about",
        "country",
    ]
    list_filter = [
        "name",
        "website",
        "popular_courses",
        "address",
        "about",
        "country",
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(University, UniversityAdmin)

# import_courses_from_csv("staticfiles/canada.csv")
