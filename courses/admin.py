from django.contrib import admin
from courses.models import Course
from import_export.admin import ImportExportModelAdmin


class CourseAdmin(ImportExportModelAdmin):
    list_display = [
        "university_name",
        "course_name",
        "gross_tuition_fee",
        "earliest_intake",
        "program_duration",
        "program_type",
        "state",
        "application_deadline",
    ]
    list_filter = [
        "university_name",
        "program_type",
        "state",
        "earliest_intake",
        "course_name",
    ]


admin.site.register(Course, CourseAdmin)
