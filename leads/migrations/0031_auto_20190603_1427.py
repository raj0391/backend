# Generated by Django 2.2.1 on 2019-06-03 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0030_products_sub_category_id_sel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Child_Category_Id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='Image_six',
        ),
        migrations.RemoveField(
            model_name='products',
            name='Sub_Category_Id_sel',
        ),
    ]
