# Generated by Django 4.1.6 on 2023-04-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0006_remove_event_reg_tbl_cpass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_reg_tbl',
            name='ticker_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
