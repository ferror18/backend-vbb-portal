# Generated by Django 3.0.10 on 2020-11-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
