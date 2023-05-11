from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import CommentViewSet, PostViewSet, CategoryViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',
        description="API for movies",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@movies.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('posts/<int:pk>/video/', PostViewSet.as_view({'get': 'get_video'}), name='post-video'),
    path('posts/<int:pk>/image/', PostViewSet.as_view({'get': 'get_image'}), name='post-image'),
]
