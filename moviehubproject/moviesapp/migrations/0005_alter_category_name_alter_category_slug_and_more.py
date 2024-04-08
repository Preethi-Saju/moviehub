# Generated by Django 4.2.9 on 2024-04-08 08:18

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0004_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.TextField(default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moviesapp.category'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(verbose_name=django.db.models.fields.DateTimeField),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(default=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='youtube',
            field=models.URLField(default=True),
        ),
    ]
