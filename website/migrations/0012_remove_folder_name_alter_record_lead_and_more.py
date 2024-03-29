# Generated by Django 4.2.7 on 2024-01-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_remove_folder_creator_remove_folder_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='name',
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Stefan', 'Stefan'), ('Benjamin', 'BENJAMIN'), ('Jakob', 'JAKOB'), ('Thomas', 'THOMAS'), ('Magnus', 'MAGNUS'), ('Vælg', 'Vælg')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Negotiation', 'NEGOTIATION'), ('Lead', 'LEAD'), ('Vælg', 'Vælg'), ('Lukket aftale', 'LUKKET AFTALE'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Lost', 'LOST')], default='Vælg', max_length=20),
        ),
    ]
