# Generated by Django 3.2.9 on 2021-11-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instructorinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128)),
                ('age', models.FloatField()),
                ('city', models.CharField(max_length=128)),
                ('bio', models.TextField()),
                ('submitted_forms', models.IntegerField()),
            ],
        ),
    ]
