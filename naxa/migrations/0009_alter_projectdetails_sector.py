# Generated by Django 4.1.5 on 2023-01-13 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('naxa', '0008_alter_projectdetails_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector', to='naxa.sector'),
        ),
    ]
