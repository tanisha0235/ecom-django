# Generated by Django 5.0.2 on 2024-02-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
