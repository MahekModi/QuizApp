# Generated by Django 4.2.9 on 2024-01-17 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_quiztopic"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="topic",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.quiztopic",
            ),
        ),
    ]
