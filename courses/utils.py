import csv
from datetime import datetime
from courses.models import Course, University


def import_courses_from_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            university_name = row["university"]
            university, _ = University.objects.get_or_create(name=university_name)

            Course.objects.create(
                university=university,
                course_name=row["course_name"],
                gross_tuition_fee=row["gross_tuition_fee"],
                cost_of_living=row["cost_of_living"],
                earliest_intake=row["earliest_intake"],
                program_duration=row["program_duration"],
                program_type=row["program_type"],
                application_deadline=row["application_deadline"],
            )
