# Generated by Django 4.2.2 on 2023-06-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name:')),
                ('surname', models.CharField(max_length=150, verbose_name='Name:')),
                ('pay', models.BooleanField(default=True, verbose_name='Pay/Notpay')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
