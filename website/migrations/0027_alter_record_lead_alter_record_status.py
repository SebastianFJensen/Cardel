# Generated by Django 4.2.7 on 2024-01-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_file_files_alter_record_lead_alter_record_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Jakob', 'JAKOB'), ('Stefan', 'Stefan'), ('Thomas', 'THOMAS'), ('Vælg', 'Vælg'), ('Magnus', 'MAGNUS'), ('Benjamin', 'BENJAMIN')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Lost', 'LOST'), ('Lukket aftale', 'LUKKET AFTALE'), ('Vælg', 'Vælg'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Negotiation', 'NEGOTIATION'), ('Lead', 'LEAD')], default='Vælg', max_length=20),
        ),
    ]
