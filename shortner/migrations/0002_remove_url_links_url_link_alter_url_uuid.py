# Generated by Django 4.0.3 on 2022-03-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='links',
        ),
        migrations.AddField(
            model_name='url',
            name='link',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
