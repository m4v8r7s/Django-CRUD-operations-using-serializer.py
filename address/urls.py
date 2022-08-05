from rest_framework.routers import DefaultRouter
from .views import AddressView
from django.urls import path, include

routers = DefaultRouter()
routers.register('address', AddressView)


urlpatterns = [
    path('api/', include(routers.urls)),
]