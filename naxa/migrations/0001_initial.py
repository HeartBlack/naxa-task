# Generated by Django 4.1.5 on 2023-01-13 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=255)),
                ('type_of', models.CharField(max_length=255)),
                ('implementing_patner', models.CharField(max_length=255)),
                ('humanitarian', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=155)),
                ('District', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=255)),
                ('sector_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projectdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('doner', models.CharField(max_length=255)),
                ('agreement_date', models.DateField()),
                ('date_of', models.DateField()),
                ('commitments', models.CharField(max_length=255)),
                ('budget_type', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naxa.agency')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naxa.location')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naxa.sector')),
            ],
        ),
    ]
