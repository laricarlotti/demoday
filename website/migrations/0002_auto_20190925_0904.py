# Generated by Django 2.2.3 on 2019-09-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Email'),
        ),
    ]
