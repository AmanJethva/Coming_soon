# Generated by Django 4.0.4 on 2022-05-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='email',
            field=models.CharField(default=0, max_length=122),
        ),
    ]
