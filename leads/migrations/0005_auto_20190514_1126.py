# Generated by Django 2.1.7 on 2019-05-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20190514_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Updated_at',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]
