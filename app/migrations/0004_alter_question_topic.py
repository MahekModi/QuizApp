# Generated by Django 4.2.9 on 2024-01-17 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_question_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.quiztopic"
            ),
        ),
    ]
