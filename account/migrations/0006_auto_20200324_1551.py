# Generated by Django 3.0.2 on 2020-03-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200324_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], default='pending', max_length=255),
        ),
    ]
