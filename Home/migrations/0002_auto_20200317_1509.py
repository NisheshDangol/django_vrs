# Generated by Django 3.0.2 on 2020-03-17 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='uploaded_by',
        ),
        migrations.DeleteModel(
            name='Bikes',
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
    ]
