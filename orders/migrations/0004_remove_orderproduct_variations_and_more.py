# Generated by Django 4.1.7 on 2023-04-24 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('orders', '0003_rename_ordered_at_orderproduct_ordered_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variations',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
        ),
    ]
