# Generated by Django 4.1.4 on 2022-12-19 10:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hall_num', models.IntegerField()),
                ('SeatAmount', models.IntegerField()),
                ('Hall_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('start_date', models.TimeField()),
                ('end_date', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='ticket.guest')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='ticket.hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='ticket.movie')),
            ],
        ),
        migrations.AddField(
            model_name='hall',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='ticket.movie'),
        ),
    ]
