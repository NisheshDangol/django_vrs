# Generated by Django 3.0.2 on 2020-03-17 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='phone',
            field=models.BigIntegerField(),
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
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]