# Generated by Django 3.2.18 on 2023-04-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_reporter', '0006_alter_manufacturer_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittedReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts', models.CharField(max_length=100)),
                ('order_date', models.DateField(max_length=100)),
                ('order_number', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
