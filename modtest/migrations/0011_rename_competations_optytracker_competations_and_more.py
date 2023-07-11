# Generated by Django 4.1.10 on 2023-07-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modtest', '0010_rename_competations_optytracker_competations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='optytracker',
            old_name='competations',
            new_name='Competations',
        ),
        migrations.RenameField(
            model_name='optytracker',
            old_name='microservices',
            new_name='Microservices',
        ),
        migrations.AlterField(
            model_name='accelerator',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='optyacc',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='optytracker',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]