# Generated by Django 2.2.17 on 2021-11-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat_box", "0006_userroom"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userroom",
            name="last_seen",
            field=models.DateTimeField(auto_now_add=True, verbose_name="last seen"),
        ),
    ]
