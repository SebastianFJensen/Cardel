# Generated by Django 4.2.7 on 2024-01-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_folder_folder_type_alter_record_lead_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Thomas', 'THOMAS'), ('Stefan', 'Stefan'), ('Magnus', 'MAGNUS'), ('Vælg', 'Vælg'), ('Benjamin', 'BENJAMIN'), ('Jakob', 'JAKOB')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Negotiation', 'NEGOTIATION'), ('Lead', 'LEAD'), ('Vælg', 'Vælg'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Lukket aftale', 'LUKKET AFTALE'), ('Lost', 'LOST')], default='Vælg', max_length=20),
        ),
    ]
