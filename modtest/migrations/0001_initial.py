# Generated by Django 4.2.2 on 2023-07-05 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accelerator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acc_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OptyTracker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('op_id', models.IntegerField()),
                ('op_name', models.CharField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OptyAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modtest.accelerator')),
                ('opty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modtest.optytracker')),
            ],
        ),
    ]