from django.urls import include, path
from rest_framework.routers import DefaultRouter

from schedule.views import ScrollView, DateView

router = DefaultRouter()

router.register('scroll', ScrollView)
router.register('date', DateView)

urlpatterns = [
    path('', include(router.urls)),
]
