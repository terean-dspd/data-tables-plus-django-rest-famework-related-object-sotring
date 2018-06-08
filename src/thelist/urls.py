from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apiviews import OrderApiView, ClientApiView
from .views import ViewOrderList

app_name = 'thelist'

router = DefaultRouter()
router.register(r'client', ClientApiView)
router.register(r'order', OrderApiView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('orders/', ViewOrderList.as_view()),
]
