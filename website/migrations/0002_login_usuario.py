# Generated by Django 2.2.3 on 2019-09-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='usuario',
            field=models.CharField(default='', max_length=100, verbose_name='Nome de Usuário'),
        ),
    ]
