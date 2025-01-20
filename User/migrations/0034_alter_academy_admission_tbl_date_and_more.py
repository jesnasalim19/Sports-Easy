# Generated by Django 4.1.6 on 2023-04-27 10:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0008_slot_tbl_amount'),
        ('User', '0033_alter_academy_admission_tbl_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy_admission_tbl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 16, 26, 23, 877730)),
        ),
        migrations.AlterField(
            model_name='book_event_tbl',
            name='bookingdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 16, 26, 23, 877730)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 16, 26, 23, 877730)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 16, 26, 23, 877730)),
        ),
        migrations.CreateModel(
            name='turf_booking_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('tdate', models.DateTimeField(default=datetime.datetime(2023, 4, 27, 16, 26, 23, 877730))),
                ('bdate', models.DateField()),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default='unpaid', max_length=25)),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Turf.turf_reg_tbl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_regtbl')),
            ],
        ),
    ]
