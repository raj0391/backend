# Generated by Django 2.2.1 on 2019-06-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_auto_20190601_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Category_Id',
            field=models.IntegerField(),
        ),
    ]