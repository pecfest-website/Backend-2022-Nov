# Generated by Django 4.1.1 on 2022-11-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0007_club_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="subcategory",
            field=models.CharField(
                choices=[
                    ("DANCE", "dance event"),
                    ("MUSIC", "music event"),
                    ("CODING", "coding event"),
                    ("HARDWARE", "hardware event"),
                    ("ART", "art event"),
                    ("PHOTOGRAPHY", "photography event"),
                    ("CINEMATOGRAPHY", "cinematography event"),
                    ("LITERARY", "literary event"),
                    ("QUIZ", "quiz event"),
                    ("DRAMATICS", "dramatics event"),
                    ("GAMING", "gaming event"),
                ],
                default="DANCE",
                max_length=15,
            ),
        ),
    ]
