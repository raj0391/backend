# Generated by Django 2.2.1 on 2019-06-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_auto_20190601_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Category_Id',
            field=models.IntegerField(),
        ),
    ]
