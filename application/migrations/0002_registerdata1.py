# Generated by Django 5.0.4 on 2024-05-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterData1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobilenumber', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]