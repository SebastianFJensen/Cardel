# Generated by Django 4.2.7 on 2024-01-22 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_folder_record_alter_record_lead_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='record',
        ),
        migrations.AddField(
            model_name='folder',
            name='foldername',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='folderuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.record'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Stefan', 'Stefan'), ('Thomas', 'THOMAS'), ('Magnus', 'MAGNUS'), ('Vælg', 'Vælg'), ('Benjamin', 'BENJAMIN'), ('Jakob', 'JAKOB')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Negotiation', 'NEGOTIATION'), ('Lukket aftale', 'LUKKET AFTALE'), ('Lost', 'LOST'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Vælg', 'Vælg'), ('Lead', 'LEAD')], default='Vælg', max_length=20),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='Files')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.folder')),
            ],
        ),
    ]
