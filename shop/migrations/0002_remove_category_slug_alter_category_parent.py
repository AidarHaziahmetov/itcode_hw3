# Generated by Django 5.1.1 on 2024-10-07 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.category",
                verbose_name="Родительская категория",
            ),
        ),
    ]
