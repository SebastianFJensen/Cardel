# Generated by Django 4.2.7 on 2024-01-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_remove_file_files_alter_record_lead_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Stefan', 'Stefan'), ('Benjamin', 'BENJAMIN'), ('Vælg', 'Vælg'), ('Jakob', 'JAKOB'), ('Thomas', 'THOMAS'), ('Magnus', 'MAGNUS')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Negotiation', 'NEGOTIATION'), ('Vælg', 'Vælg'), ('Lead', 'LEAD'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Lost', 'LOST'), ('Lukket aftale', 'LUKKET AFTALE')], default='Vælg', max_length=20),
        ),
    ]