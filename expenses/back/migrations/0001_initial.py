# Generated by Django 3.1.1 on 2020-10-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
