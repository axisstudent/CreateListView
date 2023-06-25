# Generated by Django 4.2.2 on 2023-06-25 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='surname',
            field=models.CharField(max_length=150, verbose_name='Surname:'),
        ),
    ]