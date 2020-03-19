from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from leads.models import Lead
from leads.models import Category
from leads.models import Sub_Category
from leads.models import Child_Category
from leads.models import Products
from leads.models import UserRegister
from leads.models import ViewCart

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        depth = 1
        # fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Sub_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = '__all__'


class Child_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Category
        fields = '__all__'


class Products_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
        lookup_field = ('Category_Id_id', 'Sub_Category_Id',
                        'Child_Category_Id')
        # depth = 1


class Products_SerializerSel(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
        lookup_field = ('Category_Id_id', 'Sub_Category_Id',
                        'Child_Category_Id')
        depth = 1


class Products_SerializerSel_menu(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
        lookup_field = ('Category_Id_id', 'Sub_Category_Id',
                        'Child_Category_Id')
        depth = 1

# register user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '__all__'
        write_only_fields = ('Password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserRegister.objects.create(

            Name=validated_data['Name'],
            Email=validated_data['Email'],
            Moblie=validated_data['Moblie']

        )

        user.Password = make_password('Password')
        user.save()

        return user



#  view cart status 1
class ViewCart_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ViewCart
        fields = '__all__'

#  view cart save for later
class SaveForLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewCart
        fields = '__all__'

        




























class SingleSelectedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
        lookup_field = ('Category_Id_id', 'Sub_Category_Id',
                        'Child_Category_Id')
        depth = 1
