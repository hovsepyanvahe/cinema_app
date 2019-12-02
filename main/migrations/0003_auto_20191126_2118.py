# Generated by Django 2.2.6 on 2019-11-26 21:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191021_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=50, null=True)),
                ('phone_number', models.TextField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('name', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('capacity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('timestamp', models.TimeField(default=datetime.date(2019, 11, 26))),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(null=True)),
                ('seat', models.IntegerField(null=True)),
                ('hall_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Halls')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Orders')),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Seats')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, null=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Halls')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movies')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='schedule_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Schedules'),
        ),
        migrations.CreateModel(
            name='OrderedSeats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Orders')),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Seats')),
            ],
        ),
    ]
