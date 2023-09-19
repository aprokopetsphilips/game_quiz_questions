# Generated by Django 4.2.5 on 2023-09-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_question', models.IntegerField(unique=True)),
                ('text_question', models.TextField()),
                ('text_answer', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]