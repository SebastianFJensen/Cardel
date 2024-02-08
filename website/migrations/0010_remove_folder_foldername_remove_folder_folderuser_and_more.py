# Generated by Django 4.2.7 on 2024-01-22 22:21

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_folder_name_remove_folder_record_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='foldername',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='folderuser',
        ),
        migrations.AddField(
            model_name='folder',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.record'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='website.folder'),
        ),
        migrations.AddField(
            model_name='folder',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='Lead',
            field=models.CharField(choices=[('Magnus', 'MAGNUS'), ('Jakob', 'JAKOB'), ('Stefan', 'Stefan'), ('Vælg', 'Vælg'), ('Benjamin', 'BENJAMIN'), ('Thomas', 'THOMAS')], default='Vælg', max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='Status',
            field=models.CharField(choices=[('Lukket aftale', 'LUKKET AFTALE'), ('Negotiation', 'NEGOTIATION'), ('Vælg', 'Vælg'), ('Lost', 'LOST'), ('Sendt til DLA', 'SENDT TIL DLA'), ('Lead', 'LEAD')], default='Vælg', max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
