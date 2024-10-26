# Generated by Django 5.1.2 on 2024-10-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
