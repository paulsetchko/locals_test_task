# Generated by Django 4.0.6 on 2022-08-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_lot_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='current_bid',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='bid',
            name='is_awarded',
            field=models.BooleanField(default=False),
        ),
    ]
