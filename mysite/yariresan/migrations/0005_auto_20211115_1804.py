# Generated by Django 3.1.3 on 2021-11-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariresan', '0004_alter_instructorinfo_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
