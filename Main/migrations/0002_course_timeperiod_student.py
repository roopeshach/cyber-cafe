# Generated by Django 4.0.3 on 2022-03-19 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('fee', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('joined_date', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('total_fee', models.IntegerField(default=0)),
                ('paid_fee', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('started', 'Started'), ('pending', 'Pending'), ('suspended', 'Suspended'), ('passed_out', 'Passed Out')], default='active', max_length=200)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('courses', models.ManyToManyField(to='Main.course')),
                ('time_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.timeperiod')),
            ],
        ),
    ]