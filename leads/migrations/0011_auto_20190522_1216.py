# Generated by Django 2.2.1 on 2019-05-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_auto_20190522_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='Created_by',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='Updated_by',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
