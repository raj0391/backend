# Generated by Django 2.2.1 on 2019-06-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0041_admin_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_register',
            name='Created_by',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='admin_register',
            name='Moblie',
            field=models.IntegerField(max_length=300),
        ),
        migrations.AlterField(
            model_name='admin_register',
            name='Updated_by',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]