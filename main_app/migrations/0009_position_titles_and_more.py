# Generated by Django 4.1.2 on 2023-01-25 16:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0008_alter_job_opps_and_referrals_pub_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Position_Titles",
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
                ("position_title_txt", models.CharField(max_length=50)),
                ("active_fg", models.BooleanField(default=False)),
                ("e_board_fg", models.BooleanField(default=False)),
                ("description_txt", models.TextField(max_length=250)),
                (
                    "job_family_txt",
                    models.CharField(
                        choices=[
                            ("FI", "Finance"),
                            ("CS", "Community Service"),
                            ("FU", "Fundraising"),
                            ("SH", "Sisterhood"),
                            ("IN", "Intake"),
                            ("OP", "Operations"),
                            ("ED", "Education"),
                            ("RE", "Recruiting"),
                        ],
                        default="FI",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="chapter",
            old_name="associate_chapter",
            new_name="associate_chapter_fg",
        ),
        migrations.RenameField(
            model_name="chapter",
            old_name="chapter_school",
            new_name="chapter_school_txt",
        ),
        migrations.RenameField(
            model_name="chapter",
            old_name="chapter_status",
            new_name="chapter_status_txt",
        ),
        migrations.RenameField(
            model_name="chapter", old_name="city_state", new_name="city_state_txt",
        ),
        migrations.RenameField(
            model_name="chapter",
            old_name="greek_letter_assigned",
            new_name="greek_letter_assigned_txt",
        ),
        migrations.RenameField(
            model_name="industry", old_name="industry", new_name="industry_txt",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="company_name",
            new_name="company_name_txt",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="description",
            new_name="description_txt",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="industry",
            new_name="industry_nb",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="job_link",
            new_name="job_link_txt",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="job_title",
            new_name="job_title_txt",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="level_of_opening",
            new_name="level_of_opening_txt",
        ),
        migrations.RenameField(
            model_name="job_opps_and_referrals",
            old_name="poster",
            new_name="poster_nb",
        ),
        migrations.RenameField(
            model_name="member_experiences", old_name="chapter", new_name="chapter_nb",
        ),
        migrations.RenameField(
            model_name="member_experiences",
            old_name="sister_member",
            new_name="sister_nb",
        ),
        migrations.RenameField(
            model_name="nickname_request", old_name="name", new_name="name_txt",
        ),
        migrations.RenameField(
            model_name="nickname_request",
            old_name="nickname_approval_status",
            new_name="nickname_approval_status_txt",
        ),
        migrations.RenameField(
            model_name="nickname_request",
            old_name="nickname_meaning",
            new_name="nickname_meaning_txt",
        ),
        migrations.RenameField(
            model_name="nickname_request", old_name="pnm", new_name="pnm_nb",
        ),
        migrations.RenameField(
            model_name="nickname_request",
            old_name="requestor",
            new_name="requestor_nb",
        ),
        migrations.RenameField(
            model_name="pnm", old_name="big_sister", new_name="big_sister_nb",
        ),
        migrations.RenameField(
            model_name="pnm", old_name="first_name", new_name="first_name_txt",
        ),
        migrations.RenameField(
            model_name="pnm", old_name="last_name", new_name="last_name_txt",
        ),
        migrations.RenameField(
            model_name="pnm", old_name="process_chapter", new_name="process_chapter_nb",
        ),
        migrations.RenameField(
            model_name="sister", old_name="big_sister", new_name="big_sister_nb",
        ),
        migrations.RenameField(
            model_name="sister", old_name="chapter", new_name="chapter_nb",
        ),
        migrations.RenameField(
            model_name="sister", old_name="coach", new_name="coach_fg",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="crossing_chapter",
            new_name="crossing_chapter_nb",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="crossing_class",
            new_name="crossing_class_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="current_city", new_name="current_city_txt",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="current_company",
            new_name="current_company_txt",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="current_country",
            new_name="current_country_txt",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="current_position",
            new_name="current_position_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="current_state", new_name="current_state_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="email_address", new_name="email_address_txt",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="expertise_interests",
            new_name="expertise_interests_nb",
        ),
        migrations.RenameField(
            model_name="sister", old_name="first_name", new_name="first_name_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="last_name", new_name="last_name_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="line_number", new_name="line_nb",
        ),
        migrations.RenameField(
            model_name="sister", old_name="linkedin_url", new_name="linkedin_url_txt",
        ),
        migrations.RenameField(
            model_name="sister",
            old_name="nickname_meaning",
            new_name="nickname_meaning_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="nickname", new_name="nickname_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="status", new_name="status_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="summary", new_name="summary_txt",
        ),
        migrations.RenameField(
            model_name="sister", old_name="tree", new_name="tree_txt",
        ),
        migrations.RemoveField(model_name="member_experiences", name="position",),
        migrations.RemoveField(model_name="pnm", name="potential_line_number",),
        migrations.RemoveField(model_name="pnm", name="process_semester",),
        migrations.RemoveField(model_name="pnm", name="process_year",),
        migrations.AddField(
            model_name="job_opps_and_referrals",
            name="city_txt",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="job_opps_and_referrals",
            name="remote_role_fg",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="job_opps_and_referrals",
            name="state_txt",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="job_opps_and_referrals",
            name="pub_date",
            field=models.DateTimeField(
                auto_created=True,
                default=datetime.datetime(
                    2023, 1, 25, 16, 45, 26, 566730, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date published",
            ),
        ),
        migrations.AlterField(
            model_name="nickname_request",
            name="req_date",
            field=models.DateTimeField(
                auto_created=True,
                default=datetime.datetime(
                    2023, 1, 25, 16, 45, 26, 566383, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date requested",
            ),
        ),
        migrations.AddField(
            model_name="member_experiences",
            name="position_nb",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.position_titles",
            ),
        ),
    ]
