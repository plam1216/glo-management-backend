# Generated by Django 4.1.5 on 2023-01-09 19:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_alter_nickname_request_req_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Industry",
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
                ("industry", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="nickname_request",
            name="req_date",
            field=models.DateTimeField(
                auto_created=True,
                default=datetime.datetime(
                    2023, 1, 9, 19, 5, 41, 446960, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date requested",
            ),
        ),
        migrations.CreateModel(
            name="Job_Opps_And_Referrals",
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
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_created=True,
                        default=datetime.datetime(
                            2023, 1, 9, 19, 5, 41, 447356, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="date requested",
                    ),
                ),
                ("job_title", models.CharField(max_length=50)),
                ("company_name", models.CharField(max_length=50)),
                ("job_link", models.CharField(max_length=250)),
                (
                    "level_of_opening",
                    models.CharField(
                        choices=[
                            ("00", "Internship"),
                            ("01", "Entry"),
                            ("02", "Associate"),
                            ("03", "Analyst"),
                            ("04", "Specialist"),
                            ("05", "Manager"),
                            ("06", "Senior Manager"),
                            ("07", "Director"),
                            ("08", "Senior Director"),
                            ("09", "Executive"),
                        ],
                        default="00",
                        max_length=2,
                    ),
                ),
                ("description", models.TextField(max_length=250)),
                (
                    "industry",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main_app.industry",
                    ),
                ),
                (
                    "poster",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.sister",
                    ),
                ),
            ],
        ),
    ]
