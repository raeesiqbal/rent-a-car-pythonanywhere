# Generated by Django 4.1.1 on 2022-10-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_priceincity_priceintercity_delete_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="city",
            name="image",
            field=models.ImageField(null=True, upload_to="", verbose_name="Image"),
        ),
    ]
