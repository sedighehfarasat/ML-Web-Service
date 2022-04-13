from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register("endpoints", views.EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", views.MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", views.MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", views.MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", views.ABTestViewSet, basename="abtests")


urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    re_path(r"^api/v1/(?P<endpoint_name>.+)/predict$", views.PredictView.as_view(), name="predict"),
    re_path(r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", views.StopABTestView.as_view(), name="stop_ab"),
]