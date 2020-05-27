from django.urls import path, include
from .views import aadhaar
from rest_framework import routers

router = routers.DefaultRouter()

# router.register('api', Candidateviewset)
router.register('api', aadhaar)


urlpatterns = [
    path('', include(router.urls)),
]