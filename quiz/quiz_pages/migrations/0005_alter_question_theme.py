# Generated by Django 3.2.12 on 2023-02-19 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_pages', '0004_alter_question_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz_pages.theme'),
        ),
    ]