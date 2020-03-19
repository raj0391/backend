from django.db import models
from django.utils import timezone
# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

# category table structure


class Category(models.Model):
    CategoryName = models.CharField(max_length=100)
    Status = models.IntegerField(default=1)
    Created_by = models.CharField(max_length=300, blank=True)
    Updated_by = models.CharField(max_length=300, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)


# Sub category table structure

class Sub_Category(models.Model):
    Sub_Category_Name = models.CharField(max_length=100, blank=False)
    Category_Id = models.IntegerField(blank=False)
    Status = models.IntegerField(default=1)
    Created_by = models.CharField(max_length=300, blank=True)
    Updated_by = models.CharField(max_length=300, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

# Child category table structure


class Child_Category(models.Model):
    Child_Category_Name = models.CharField(max_length=100, blank=False)
    Category_Id = models.IntegerField(blank=False)
    Sub_Category_Id = models.IntegerField(blank=False)
    Status = models.IntegerField(default=1)
    Created_by = models.CharField(max_length=300, blank=True)
    Updated_by = models.CharField(max_length=300, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)


# Products table structure

class Products(models.Model):

    Category_Id = models.ForeignKey(Category, on_delete=models.CASCADE)
    Sub_Category_Id = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    # Child_Category_Id = models.ForeignKey(
    #     Child_Category, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=300)
    Product_Id = models.CharField(max_length=300)
    Quantity = models.IntegerField()
    Unit_Price = models.IntegerField()
    Discount = models.IntegerField()
    Offer_Price = models.IntegerField()
    Image_one = models.ImageField(upload_to="gallery")
    Image_two = models.ImageField(upload_to="gallery")
    Image_three = models.ImageField(upload_to="gallery")
    Image_four = models.ImageField(upload_to="gallery")
    Image_five = models.ImageField(upload_to="gallery")
    Image_six = models.ImageField(upload_to="gallery")
    Product_Quote = models.CharField(max_length=300)
    Product_Detail_Description = models.CharField(max_length=300)
    Status = models.IntegerField()
    Created_by = models.CharField(max_length=300)
    Updated_by = models.CharField(max_length=300)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

# User register table structure


class UserRegister(models.Model):

    Name = models.CharField(max_length=300)
    Email = models.CharField(max_length=200, unique=True)
    Moblie = models.BigIntegerField(unique=True)
    Password = models.CharField(max_length=300)
    Status = models.IntegerField(default=0)
    Created_by = models.CharField(max_length=300, blank=True)
    Updated_by = models.CharField(max_length=300, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)


# Register table structure

class ViewCart(models.Model):
    Product_Name = models.CharField(max_length=300)
    Product_Id = models.CharField(max_length=300)
    Unit_Price = models.IntegerField()
    Offer_Price = models.IntegerField()
    Image_one = models.CharField(max_length=300)
    Quantity = models.IntegerField(default=1)
    Product_Quote = models.CharField(max_length=300)
    Product_Detail_Description = models.CharField(max_length=300)
    Status = models.IntegerField(default=1)
    Created_by = models.CharField(max_length=300, blank=True)
    Updated_by = models.CharField(max_length=300, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
