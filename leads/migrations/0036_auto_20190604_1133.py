# Generated by Django 2.2.1 on 2019-06-04 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0035_auto_20190603_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Child_Category_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Child_Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='Sub_Category_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Sub_Category'),
        ),
    ]
