# Generated by Django 2.2.1 on 2019-06-03 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0029_auto_20190603_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Sub_Category_Id_sel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.Category'),
            preserve_default=False,
        ),
    ]