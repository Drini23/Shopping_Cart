from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('carts', views.CartViewSet)
urlpatterns = router.urls

