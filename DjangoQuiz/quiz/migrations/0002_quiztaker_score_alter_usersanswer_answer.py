# Generated by Django 4.1.1 on 2022-09-25 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usersanswer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.answer'),
        ),
    ]
