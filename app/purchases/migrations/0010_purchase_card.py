# Generated by Django 4.2.5 on 2023-09-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0009_alter_purchase_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='card',
            field=models.TextField(default=''),
        ),
    ]