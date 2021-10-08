# Generated by Django 3.2.6 on 2021-10-08 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0041_auto_20211008_0733'),
    ]

    operations = [
                migrations.CreateModel(
            name='PlateDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('plate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='days_plate', to='food.plate')),
            ],
        ),
    ]
