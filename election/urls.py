from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ElectionView

router = DefaultRouter()

urlpatterns = [
    path('', ElectionView.as_view(), name='elections'),
]

urlpatterns += router.urls
