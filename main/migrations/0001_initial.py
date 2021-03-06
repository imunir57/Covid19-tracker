# Generated by Django 2.2.6 on 2020-04-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('new_cases', models.IntegerField()),
                ('new_deaths', models.IntegerField()),
                ('new_recovered', models.IntegerField()),
                ('total_cases', models.IntegerField()),
                ('total_deaths', models.IntegerField()),
                ('total_recovered', models.IntegerField()),
            ],
        ),
    ]
