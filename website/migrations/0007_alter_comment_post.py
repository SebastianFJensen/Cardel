# Generated by Django 4.2.7 on 2023-11-24 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_recorddetailview_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.record'),
        ),
    ]
