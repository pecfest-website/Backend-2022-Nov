# Generated by Django 4.1.1 on 2022-11-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0008_alter_event_subcategory"),
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
                    ("FUN", "fun event"),
                ],
                default="DANCE",
                max_length=15,
            ),
        ),
    ]
