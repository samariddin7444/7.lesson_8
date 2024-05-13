from .views import ShopPageView, ShopDetailPageView, ContactPageView, ChackOutPageView, CartPageView, \
    TestimonalPageView, NotFoundPageView, SearchResulPageView, FruitPageApiView, VegetablePageApiView, \
    BestSellPageApiView
from django.urls import path,include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        description="Music Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='pipsudo@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

router = routers.DefaultRouter()
router.register('fruits', FruitPageApiView)
router.register('vegetables', VegetablePageApiView)
router.register('bestsell', BestSellPageApiView)
urlpatterns = [
    path('', include(router.urls)),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('shopdetail/', ShopDetailPageView.as_view(), name='detail'),
    path('contact/', ChackOutPageView.as_view(), name='contact'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('testimonial/', TestimonalPageView.as_view(), name='testimonial'),
    path('checkout/', ChackOutPageView.as_view(), name='checkout'),
    path('notfound/', NotFoundPageView.as_view(), name='notfound'),
    path('search/', SearchResulPageView.as_view(), name='search'),
]

