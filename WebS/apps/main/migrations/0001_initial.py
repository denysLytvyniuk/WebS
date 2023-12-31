# Generated by Django 4.2.2 on 2023-07-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=50, unique=True)),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('price_in_usd', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
    ]
