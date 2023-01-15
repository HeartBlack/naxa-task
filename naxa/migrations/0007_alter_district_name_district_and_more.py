# Generated by Django 4.1.5 on 2023-01-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naxa', '0006_alter_projectdetails_commitments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name_district',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='name_municipality',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='name_province',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
