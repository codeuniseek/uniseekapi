from django.contrib import admin
from courses.models import Course
from import_export.admin import ImportExportModelAdmin

admin.site.register(Course, ImportExportModelAdmin)
