# Generated by Django 4.1.5 on 2023-01-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_alter_books_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='authors',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='categories',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.CharField(max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='num_pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='published_year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='ratings_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='subtitle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='thumbnail',
            field=models.CharField(max_length=500, null=True),
        ),
    ]