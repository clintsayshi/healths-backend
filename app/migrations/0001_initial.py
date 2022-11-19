# Generated by Django 4.1.2 on 2022-11-18 23:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField(default=None, max_length=500)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 11, 18, 23, 35, 21, 560739, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='UserMedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 11, 18, 23, 35, 21, 561742, tzinfo=datetime.timezone.utc))),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicalcondition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('canister', models.IntegerField(max_length=50)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 11, 18, 23, 35, 21, 559744, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
