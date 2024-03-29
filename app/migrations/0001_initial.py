# Generated by Django 4.2.9 on 2024-01-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=500)),
                ("option1", models.CharField(max_length=100)),
                ("option2", models.CharField(max_length=100)),
                ("option3", models.CharField(max_length=100)),
                ("option4", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=100)),
            ],
        ),
    ]
