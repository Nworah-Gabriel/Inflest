# Generated by Django 4.2.11 on 2024-06-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflestApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='macroeconomicdata',
            name='growth_rate',
        ),
        migrations.RemoveField(
            model_name='macroeconomicdata',
            name='inf',
        ),
        migrations.AddField(
            model_name='macroeconomicdata',
            name='inflation_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macroeconomicdata',
            name='exchange_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macroeconomicdata',
            name='fdi',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macroeconomicdata',
            name='fiscal_expenditure',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macroeconomicdata',
            name='interest_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macroeconomicdata',
            name='real_gdp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='macroeconomicdata',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
