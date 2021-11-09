# Generated by Django 3.2.8 on 2021-10-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryeaisapp', '0004_auto_20211028_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='daily_reminder',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='daily_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='monthly_reminder',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='monthly_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weekly_reminder',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weekly_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yearly_reminder',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yearly_report',
            field=models.BooleanField(default=False),
        ),
    ]
