# Generated by Django 3.2.6 on 2021-08-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_alter_food_food_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='platelayout',
            name='has_dessert',
        ),
        migrations.RemoveField(
            model_name='platelayout',
            name='has_drink',
        ),
        migrations.RemoveField(
            model_name='platesection',
            name='count',
        ),
        migrations.AddField(
            model_name='plate',
            name='has_dessert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plate',
            name='has_drink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='platelayout',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='platesection',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='platesection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.RemoveField(
            model_name='platesection',
            name='category',
        ),
        migrations.AddField(
            model_name='platesection',
            name='category',
            field=models.ManyToManyField(to='food.FoodCategory'),
        ),
    ]