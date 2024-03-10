# Generated by Django 4.1.7 on 2023-04-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], max_length=10),
        ),
        migrations.AlterModelTable(
            name='book',
            table='book_table',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact_table',
        ),
        migrations.AlterModelTable(
            name='news',
            table='news_table',
        ),
    ]