# Generated by Django 3.0.2 on 2020-03-24 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='no_of_vehicle',
            field=models.IntegerField(null=True),
        ),
    ]
