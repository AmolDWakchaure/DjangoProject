# Generated by Django 3.2 on 2021-04-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='OperatingSystem',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='Price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='Processor',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='ram',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='storage',
            field=models.TextField(default=''),
        ),
    ]
