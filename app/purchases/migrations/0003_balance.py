# Generated by Django 3.2.3 on 2021-06-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_alter_purchase_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mount', models.FloatField(default=0.0)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
