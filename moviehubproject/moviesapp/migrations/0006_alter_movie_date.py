# Generated by Django 4.2.11 on 2024-04-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0005_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(),
        ),
    ]
