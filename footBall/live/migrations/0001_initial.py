# Generated by Django 2.0.5 on 2018-05-23 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_1', models.CharField(max_length=100)),
                ('guest_team_2', models.CharField(max_length=100)),
                ('stadium', models.TextField(blank=True)),
                ('commentator', models.TextField(blank=True)),
                ('link_1', models.TextField(blank=True)),
                ('link_2', models.TextField(blank=True)),
                ('link_3', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('match_Date', models.DateField()),
                ('match_time', models.TimeField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='live.Channel')),
                ('lig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='live.Lig')),
            ],
        ),
    ]
