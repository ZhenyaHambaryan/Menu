# Generated by Django 3.2.6 on 2021-08-31 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20210830_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_type', to='food.foodtype'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='layout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layout_plate', to='food.platelayout'),
        ),
    ]