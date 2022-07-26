# Generated by Django 2.2.9 on 2020-03-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0101_custom_validator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problemdata",
            name="checker",
            field=models.CharField(
                blank=True,
                choices=[
                    ("standard", "Standard"),
                    ("floats", "Floats"),
                    ("floatsabs", "Floats (absolute)"),
                    ("floatsrel", "Floats (relative)"),
                    ("rstripped", "Non-trailing spaces"),
                    ("sorted", "Unordered"),
                    ("identical", "Byte identical"),
                    ("linecount", "Line-by-line"),
                    ("custom", "Custom checker"),
                    ("customval", "Custom Validator"),
                ],
                max_length=10,
                verbose_name="checker",
            ),
        ),
        migrations.AlterField(
            model_name="problemtestcase",
            name="checker",
            field=models.CharField(
                blank=True,
                choices=[
                    ("standard", "Standard"),
                    ("floats", "Floats"),
                    ("floatsabs", "Floats (absolute)"),
                    ("floatsrel", "Floats (relative)"),
                    ("rstripped", "Non-trailing spaces"),
                    ("sorted", "Unordered"),
                    ("identical", "Byte identical"),
                    ("linecount", "Line-by-line"),
                    ("custom", "Custom checker"),
                    ("customval", "Custom Validator"),
                ],
                max_length=10,
                verbose_name="checker",
            ),
        ),
    ]
