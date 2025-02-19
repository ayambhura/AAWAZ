# Generated by Django 4.1.7 on 2023-03-20 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_users_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='latlong',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='city',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='department',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='description',
            field=models.CharField(default='Pending', max_length=1000),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='pincode',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='state',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='time',
            field=models.DateTimeField(default='2020-01-01 00:00:00+00:00'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='user_id',
            field=models.ForeignKey(default='10', on_delete=django.db.models.deletion.DO_NOTHING, to='api.users'),
        ),
    ]
