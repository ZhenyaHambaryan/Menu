# Generated by Django 3.2.6 on 2021-09-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_auto_20210906_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='foods',
            field=models.ManyToManyField(blank=True, to='food.Food'),
        ),
    ]
