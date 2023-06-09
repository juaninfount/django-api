from rest_framework import routers
from core.user.views import UserViewSet

router = routers.SimpleRouter()

# prefijo: nombre del endpoint, viewset: clase viewset, basename como opcion de legibilidad
router.register(r'user', UserViewSet, basename='user')
urlpatterns = [
    *router.urls
    ]