# Generated by Django 4.1.1 on 2022-10-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0008_bookingintercity_bookingincity"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("name", models.CharField(max_length=999, verbose_name="Name")),
                ("email", models.CharField(max_length=999, verbose_name="Email")),
                ("phone", models.CharField(max_length=999, verbose_name="Phone")),
                ("subject", models.CharField(max_length=999, verbose_name="Subject")),
                ("message", models.TextField(verbose_name="Message")),
                (
                    "date_posted",
                    models.DateTimeField(auto_now=True, verbose_name="Date Posted"),
                ),
            ],
        ),
    ]
