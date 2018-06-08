# Generated by Django 2.0.6 on 2018-06-08 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('item', models.CharField(max_length=200, verbose_name='Item')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='thelist.Client', verbose_name='Clent')),
            ],
        ),
    ]