# Generated by Django 4.2.7 on 2024-01-22 23:42

from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_folder_foldername_remove_folder_folderuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='level',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='folder',
            name='record',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='website.record'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Thomas', 'THOMAS'), ('Stefan', 'Stefan'), ('Vælg', 'Vælg'), ('Magnus', 'MAGNUS'), ('Benjamin', 'BENJAMIN'), ('Jakob', 'JAKOB')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Sendt til DLA', 'SENDT TIL DLA'), ('Negotiation', 'NEGOTIATION'), ('Lost', 'LOST'), ('Lead', 'LEAD'), ('Vælg', 'Vælg'), ('Lukket aftale', 'LUKKET AFTALE')], default='Vælg', max_length=20),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to=website.models.get_file_location)),
                ('folder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.folder')),
            ],
        ),
    ]
