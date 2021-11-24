# Generated by Django 3.2.9 on 2021-11-14 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariresan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructorinfo',
            name='age',
        ),
        migrations.RemoveField(
            model_name='instructorinfo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='instructorinfo',
            name='submitted_forms',
        ),
        migrations.AddField(
            model_name='instructorinfo',
            name='address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='instructorinfo',
            name='gender',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='instructorinfo',
            name='number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='instructorinfo',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='instructorinfo',
            name='fullname',
            field=models.CharField(max_length=128, null=True),
        ),
    ]