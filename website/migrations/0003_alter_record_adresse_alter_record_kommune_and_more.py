# Generated by Django 4.2.6 on 2023-10-28 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_rename_records_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Adresse',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='Kommune',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='Kontaktperson',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='Mail',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='Region',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
