# Generated by Django 4.1.6 on 2023-04-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_alter_booking_arrival_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['order_date']},
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(),
        ),
    ]
