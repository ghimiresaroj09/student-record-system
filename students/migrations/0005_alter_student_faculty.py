# Generated by Django 5.0.6 on 2024-06-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.CharField(max_length=50, verbose_name='Faculty'),
        ),
    ]
