from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewset
router = DefaultRouter()

router.register("", ProductViewset)
urlpatterns = router.urls
