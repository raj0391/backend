# Generated by Django 2.2.1 on 2019-05-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20190522_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
