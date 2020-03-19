# Generated by Django 2.1.7 on 2019-05-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20190514_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Child_Category_Name', models.CharField(max_length=100)),
                ('Category_Id', models.IntegerField()),
                ('Sub_Category_Id', models.IntegerField()),
                ('Status', models.IntegerField()),
                ('Created_by', models.CharField(max_length=300)),
                ('Updated_by', models.CharField(max_length=300)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Child_Category_Name', models.CharField(max_length=100)),
                ('Category_Id', models.IntegerField()),
                ('Sub_Category_Id', models.IntegerField()),
                ('Child_Category_Id', models.IntegerField()),
                ('Product_Name', models.CharField(max_length=300)),
                ('Product_Id', models.CharField(max_length=300)),
                ('Quantity', models.IntegerField()),
                ('Unit_Price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Offer_Price', models.IntegerField()),
                ('Product_Quote', models.CharField(max_length=300)),
                ('Product_Detail_Description', models.CharField(max_length=300)),
                ('Status', models.IntegerField()),
                ('Created_by', models.CharField(max_length=300)),
                ('Updated_by', models.CharField(max_length=300)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Category_Name', models.CharField(max_length=100)),
                ('Category_Id', models.IntegerField()),
                ('Status', models.IntegerField()),
                ('Created_by', models.CharField(max_length=300)),
                ('Updated_by', models.CharField(max_length=300)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
