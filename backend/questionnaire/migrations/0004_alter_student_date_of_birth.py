# Generated by Django 4.1.7 on 2023-04-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "questionnaire",
            "0003_alter_student_date_of_birth_alter_student_gender_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="date_of_birth",
            field=models.DateTimeField(null=True),
        ),
    ]
