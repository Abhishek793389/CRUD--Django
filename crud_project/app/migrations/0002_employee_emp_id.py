# Generated by Django 5.1 on 2024-09-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(db_column='Emp ID', max_length=20, null=True, unique=True),
        ),
    ]
