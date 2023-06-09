# Generated by Django 4.1.7 on 2023-03-29 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("logo", models.ImageField(upload_to="logo_empresa")),
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("headquarters", models.CharField(max_length=30)),
                (
                    "marketing_niche",
                    models.CharField(
                        choices=[
                            ("M", "Marketing"),
                            ("T", "Tecnologia"),
                            ("N", "Nutrição"),
                            ("D", "Design"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Specializations",
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
                ("specialization", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Technologies",
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
                ("technology", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Jobs",
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
                ("title", models.CharField(max_length=30)),
                (
                    "experience",
                    models.CharField(
                        choices=[("J", "Júnior"), ("P", "Pleno"), ("S", "Sênior")],
                        max_length=2,
                    ),
                ),
                ("final_date", models.DateField()),
                ("position_type", models.TimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("I", "Interesse"),
                            ("C", "Currículo enviado"),
                            ("E", "Entrevista"),
                            ("D", "Desafio técnico"),
                            ("F", "Finalizado"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="empresas.company",
                    ),
                ),
                (
                    "technologies_mastered",
                    models.ManyToManyField(to="empresas.technologies"),
                ),
                (
                    "technologies_study",
                    models.ManyToManyField(
                        related_name="estudar", to="empresas.technologies"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="specializations",
            field=models.ManyToManyField(to="empresas.specializations"),
        ),
        migrations.AddField(
            model_name="company",
            name="technologies",
            field=models.ManyToManyField(to="empresas.technologies"),
        ),
    ]
