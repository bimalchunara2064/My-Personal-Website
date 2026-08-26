from django.db import migrations


def create_default_courses(apps, schema_editor):
    training_service = apps.get_model("hero", "TrainingService")
    course_model = apps.get_model("hero", "Course")
    service = training_service.objects.first()
    if not service:
        service = training_service.objects.create()

    courses = [
        {
            "icon": "🖥️",
            "title": "Basic Computer Training",
            "description": "Computer fundamentals, Windows, MS Office, typing, and internet skills.",
            "duration": "1-2 Months",
            "order": 1,
        },
        {
            "icon": "🌐",
            "title": "Website Design",
            "description": "HTML, CSS, JavaScript, responsive design, Bootstrap and practical website projects.",
            "duration": "2-3 Months",
            "order": 2,
        },
        {
            "icon": "🐍",
            "title": "Python Development",
            "description": "Python programming, Django basics, databases and real-world application development.",
            "duration": "3 Months",
            "order": 3,
        },
    ]

    for course in courses:
        course_model.objects.get_or_create(
            service=service,
            title=course["title"],
            defaults=course,
        )


def remove_default_courses(apps, schema_editor):
    course_model = apps.get_model("hero", "Course")
    course_model.objects.filter(
        title__in=[
            "Basic Computer Training",
            "Website Design",
            "Python Development",
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("hero", "0006_course_trainingservice_enrollment_course_service"),
    ]

    operations = [
        migrations.RunPython(create_default_courses, remove_default_courses),
    ]
