# Generated by Django 4.1.1 on 2022-10-10 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_city_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookingInterCity",
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
                ("address", models.CharField(max_length=999, verbose_name="Address")),
                (
                    "pickup_date",
                    models.CharField(max_length=999, verbose_name="Pickup Date"),
                ),
                (
                    "pickup_time",
                    models.CharField(max_length=999, verbose_name="Pickup Time"),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Phone"
                    ),
                ),
                (
                    "Status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In Progress", "In progress"),
                            ("Completed", "Completed"),
                            ("Cancelled", "Cancelled"),
                        ],
                        default="Pending",
                        max_length=99,
                        verbose_name="Status",
                    ),
                ),
                (
                    "date_posted",
                    models.DateTimeField(auto_now=True, verbose_name="Date Posted"),
                ),
                (
                    "price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.priceintercity",
                        verbose_name="Price",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookingInCity",
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
                ("address", models.CharField(max_length=999, verbose_name="Address")),
                (
                    "pickup_date",
                    models.CharField(max_length=999, verbose_name="Pickup Date"),
                ),
                (
                    "pickup_time",
                    models.CharField(max_length=999, verbose_name="Pickup Time"),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Phone"
                    ),
                ),
                (
                    "Status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In Progress", "In progress"),
                            ("Completed", "Completed"),
                            ("Cancelled", "Cancelled"),
                        ],
                        default="Pending",
                        max_length=99,
                        verbose_name="Status",
                    ),
                ),
                (
                    "date_posted",
                    models.DateTimeField(auto_now=True, verbose_name="Date Posted"),
                ),
                (
                    "price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.priceincity",
                        verbose_name="Price",
                    ),
                ),
            ],
        ),
    ]