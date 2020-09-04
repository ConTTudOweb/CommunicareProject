from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .core.api.views import EventViewSet, TestimonyViewSet, ContactViewSet

if settings.DEBUG:
    router = DefaultRouter(trailing_slash=False)
else:
    router = SimpleRouter(trailing_slash=False)

router.register("events", EventViewSet)
router.register("testimonials", TestimonyViewSet)
router.register("contacts", ContactViewSet, basename='contact')


app_name = "api"
urlpatterns = router.urls
