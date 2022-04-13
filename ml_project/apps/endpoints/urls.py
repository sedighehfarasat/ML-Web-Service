from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register("endpoints", views.EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", views.MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", views.MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", views.MLRequestViewSet, basename="mlrequests")


urlpatterns = [
    path("api/v1/", include(router.urls)),
]