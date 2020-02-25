# Generated by Django 3.0.2 on 2020-02-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('cc', models.IntegerField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('available', models.BooleanField(default='True')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('seat', models.IntegerField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('available', models.BooleanField(default='True')),
            ],
        ),
    ]