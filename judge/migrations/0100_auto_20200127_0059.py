# Generated by Django 2.2.9 on 2020-01-27 00:59

import django.core.validators
from django.db import migrations, models
import judge.models.problem_data
import judge.utils.problem_data


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0099_custom_checker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problemdata",
            name="custom_checker",
            field=models.FileField(
                blank=True,
                null=True,
                storage=judge.utils.problem_data.ProblemDataStorage(),
                upload_to=judge.models.problem_data.problem_directory_file,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["py"]
                    )
                ],
                verbose_name="custom checker file",
            ),
        ),
    ]
