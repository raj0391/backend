
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework import routers
from .api import LeadViewSet
from .api import CategoryViewSet
from .api import Sub_CategoryViewSet
from .api import Child_CategoryViewSet
from .api import ProductsViewSet
from .api import ProductsViewSetSel
from .api import ProductsViewSetSel_menu
from .api import UserViewSet
from .api import SingleSelectedViewSet
from .api import ViewCartViewSet
from .api import SaveForLaterViewSet
# from .api import Category_SelViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/Category', CategoryViewSet, 'Category')
router.register('api/Sub_Category', Sub_CategoryViewSet, 'Sub_Category')
# router.register('api/Sub_Category/<pk>', Sub_CategoryViewSet, 'Sub_Category')
router.register('api/Child_Category', Child_CategoryViewSet, 'Child_Category')
router.register('api/Products', ProductsViewSet, 'Products')
router.register('api/get/Products', ProductsViewSetSel, 'ProductsSel')
router.register('api/sel/get/Products',
                ProductsViewSetSel_menu, 'ProductsViewSetSel_menu')
router.register('api/User_register', UserViewSet, 'UserView')
router.register('api/View_cart', ViewCartViewSet, 'ViewCartView')
router.register('api/SaveForLater', SaveForLaterViewSet, 'SaveForLater')


router.register('api/SingleSelected', SingleSelectedViewSet, 'SingleSelected')

urlpatterns = router.urls
