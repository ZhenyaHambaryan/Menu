# Generated by Django 3.2.4 on 2021-07-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlateLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('entree_count', models.IntegerField()),
                ('has_drink', models.BooleanField(default=True)),
                ('has_dessert', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_field', models.IntegerField()),
                ('layout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.platelayout')),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('food_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.foodcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('ingredients', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.IntegerField()),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_healthy', models.BooleanField(default=False)),
                ('food_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.foodtype')),
            ],
        ),
    ]
