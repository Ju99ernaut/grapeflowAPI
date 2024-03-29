# Generated by Django 3.0.3 on 2020-04-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200416_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='assets',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AddField(
            model_name='block',
            name='components',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AddField(
            model_name='block',
            name='styles',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='block',
            name='css',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='block',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='block',
            name='html',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='block',
            name='script',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='logic',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='logic',
            name='script',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='assets',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='page',
            name='components',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='page',
            name='css',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='html',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='styles',
            field=models.TextField(blank=True, default='[]'),
        ),
    ]
