# Generated by Django 3.0.3 on 2020-04-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200421_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='preview',
            field=models.ImageField(default='0', upload_to=''),
        ),
    ]