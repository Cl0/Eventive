# Generated by Django 2.2.5 on 2019-11-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name='start time and date')),
                ('end_time', models.DateTimeField(verbose_name='end time and date')),
                ('categories', models.ManyToManyField(related_name='events', to='eventFinderApp.Category')),
            ],
        ),
    ]
