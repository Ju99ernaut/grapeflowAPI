# Generated by Django 3.0.3 on 2020-07-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200523_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='height',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='asset',
            name='width',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.ImageField(default='0', height_field='height', upload_to='', width_field='width'),
        ),
    ]
