# Generated by Django 2.2.17 on 2021-05-24 19:22

from django.db import migrations, models


def hide_scoreboard_eq_true(apps, schema_editor):
    Contest = apps.get_model("judge", "Contest")
    Contest.objects.filter(hide_scoreboard=True).update(scoreboard_visibility="C")


def scoreboard_visibility_eq_contest(apps, schema_editor):
    Contest = apps.get_model("judge", "Contest")
    Contest.objects.filter(scoreboard_visibility__in=("C", "P")).update(
        hide_scoreboard=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0114_auto_20201228_1041"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contest",
            options={
                "permissions": (
                    ("see_private_contest", "See private contests"),
                    ("edit_own_contest", "Edit own contests"),
                    ("edit_all_contest", "Edit all contests"),
                    ("clone_contest", "Clone contest"),
                    ("moss_contest", "MOSS contest"),
                    ("contest_rating", "Rate contests"),
                    ("contest_access_code", "Contest access codes"),
                    ("create_private_contest", "Create private contests"),
                    ("change_contest_visibility", "Change contest visibility"),
                    ("contest_problem_label", "Edit contest problem label script"),
                ),
                "verbose_name": "contest",
                "verbose_name_plural": "contests",
            },
        ),
        migrations.RemoveField(
            model_name="contest",
            name="hide_scoreboard",
        ),
        migrations.RemoveField(
            model_name="contest",
            name="organizers",
        ),
        migrations.AddField(
            model_name="contest",
            name="authors",
            field=models.ManyToManyField(
                help_text="These users will be able to edit the contest.",
                related_name="_contest_authors_+",
                to="judge.Profile",
            ),
        ),
        migrations.AddField(
            model_name="contest",
            name="curators",
            field=models.ManyToManyField(
                blank=True,
                help_text="These users will be able to edit the contest, but will not be listed as authors.",
                related_name="_contest_curators_+",
                to="judge.Profile",
            ),
        ),
        migrations.AddField(
            model_name="contest",
            name="problem_label_script",
            field=models.TextField(
                blank=True,
                help_text="A custom Lua function to generate problem labels. Requires a single function with an integer parameter, the zero-indexed contest problem index, and returns a string, the label.",
                verbose_name="contest problem label script",
            ),
        ),
        migrations.AddField(
            model_name="contest",
            name="scoreboard_visibility",
            field=models.CharField(
                choices=[
                    ("V", "Visible"),
                    ("C", "Hidden for duration of contest"),
                    ("P", "Hidden for duration of participation"),
                ],
                default="V",
                help_text="Scoreboard visibility through the duration of the contest",
                max_length=1,
                verbose_name="scoreboard visibility",
            ),
        ),
        migrations.AddField(
            model_name="contest",
            name="testers",
            field=models.ManyToManyField(
                blank=True,
                help_text="These users will be able to view the contest, but not edit it.",
                related_name="_contest_testers_+",
                to="judge.Profile",
            ),
        ),
        migrations.AddField(
            model_name="contestparticipation",
            name="tiebreaker",
            field=models.FloatField(default=0.0, verbose_name="tie-breaking field"),
        ),
    ]
