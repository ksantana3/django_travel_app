# Generated by Django 2.2.1 on 2019-05-28 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_trips', to='logreg.User')),
                ('trip_members', models.ManyToManyField(related_name='joined_trips', to='logreg.User')),
            ],
        ),
    ]
