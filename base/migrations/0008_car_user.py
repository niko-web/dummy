# Generated by Django 4.2.4 on 2023-09-08 03:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_user_siteuser_remove_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='base.siteuser'),
            preserve_default=False,
        ),
    ]