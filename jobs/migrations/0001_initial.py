# Generated by Django 3.2.5 on 2021-07-21 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=100)),
                ('experience_level', models.CharField(choices=[('Internship', 'Internship'), ('Entry', 'Entry'), ('Associate', 'Associate'), ('Mid-Senior', 'Mid-Senior'), ('Director', 'Director'), ('Executive', 'Executive')], max_length=25)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('qualifications', models.TextField()),
                ('compensation_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compensation_rate', models.CharField(choices=[('Hourly', 'Hourly'), ('Yearly', 'Yearly')], max_length=10)),
            ],
        ),
    ]