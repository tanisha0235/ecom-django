# Generated by Django 5.0.2 on 2024-02-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_alter_brand_detail_avgprice_final_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='final_detail',
            name='image',
            field=models.CharField(default='', max_length=500),
        ),
    ]
