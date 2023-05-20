# Generated by Django 4.1.7 on 2023-04-20 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("questionnaire", "0007_alter_behaviors_behavior_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="email_verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                unique=True,
            ),
        ),
    ]
