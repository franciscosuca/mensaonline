# Generated by Django 2.2.1 on 2019-06-17 08:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20190617_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]
