# Generated by Django 3.2.18 on 2023-04-29 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders_reporter', '0007_submittedreport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubmittedReport',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='model',
            new_name='order_number',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='omsid',
            new_name='parts',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='parts_usage',
            new_name='sku',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='store_sku',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='store_so_sku',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='vendor',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
