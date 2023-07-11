# Generated by Django 4.2.2 on 2023-07-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modtest', '0009_alter_competation_id_alter_microservice_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='optytracker',
            old_name='Competations',
            new_name='competations',
        ),
        migrations.RenameField(
            model_name='optytracker',
            old_name='Microservices',
            new_name='microservices',
        ),
        migrations.AlterField(
            model_name='accelerator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='optyacc',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='optytracker',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
