# Generated by Django 4.1.5 on 2023-01-13 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naxa', '0005_alter_projectdetails_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='commitments',
            field=models.FloatField(max_length=255),
        ),
    ]
