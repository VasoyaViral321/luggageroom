# Generated by Django 3.2 on 2021-04-18 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210416_1925'),
        ('booking', '0008_auto_20210416_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=5)),
                ('city_name', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.FloatField(default=1000.0)),
                ('storage_location', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('room_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.admin')),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.storages'),
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
