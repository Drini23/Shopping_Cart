# Generated by Django 5.0.1 on 2024-01-21 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='api.product'),
        ),
    ]