from rest_framework.routers import DefaultRouter
from .views import ShortenerListAPIView
router = DefaultRouter()
router.register('', ShortenerListAPIView)
urlpatterns = router.urls
