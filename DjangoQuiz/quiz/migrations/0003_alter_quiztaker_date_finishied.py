# Generated by Django 4.1.1 on 2022-09-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiztaker_score_alter_usersanswer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiztaker',
            name='date_finishied',
            field=models.DateTimeField(null=True),
        ),
    ]