from django.contrib.auth.hashers import make_password
from leads.models import Lead
from leads.models import Category
from leads.models import Sub_Category
from leads.models import Child_Category
from leads.models import Products
from leads.models import UserRegister
from leads.models import ViewCart

from .serializers import LeadSerializer
from .serializers import CategorySerializer
from .serializers import Sub_Category_Serializer
from .serializers import Child_Category_Serializer
from .serializers import Products_Serializer
from .serializers import Products_SerializerSel
from .serializers import Products_SerializerSel_menu
from .serializers import UserSerializer
from .serializers import ViewCart_Serializer

from .serializers import SaveForLaterSerializer


from .serializers import SingleSelectedSerializer

# from .serializers import LoginSerializer


# delete delete delete delete delete delete delete

# from .serializers import Category_Sel_Serializer

# delete delete delete delete delete delete delete


from rest_framework import viewsets, permissions, generics
from url_filter.integrations.drf import DjangoFilterBackend
# from django.shortcuts import renders


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['CategoryName', 'id']

    serializer_class = CategorySerializer


class Sub_CategoryViewSet(viewsets.ModelViewSet):
    queryset = Sub_Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'Category_Id', 'Sub_Category_Name']
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = Sub_Category_Serializer


class Child_CategoryViewSet(viewsets.ModelViewSet):
    queryset = Child_Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'Category_Id',
                     'Sub_Category_Id', 'Child_Category_Name']
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = Child_Category_Serializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Products_Serializer


class ProductsViewSetSel(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Products_SerializerSel


class ProductsViewSetSel_menu(viewsets.ModelViewSet):
    serializer_class = Products_SerializerSel_menu
    def get_queryset(self):

        queryset_list = Products.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Sub_Category_Id__id=query).distinct()
            return queryset_list


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ViewCartViewSet(viewsets.ModelViewSet):
    queryset = ViewCart.objects.filter(Status='1')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ViewCart_Serializer


class SaveForLaterViewSet(viewsets.ModelViewSet):
    queryset = ViewCart.objects.filter(Status='0')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SaveForLaterSerializer


class SingleSelectedViewSet(viewsets.ModelViewSet):
    serializer_class = SingleSelectedSerializer
    def get_queryset(self):

        queryset_list = Products.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                id=query).distinct()
            return queryset_list
