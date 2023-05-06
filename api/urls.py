from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet, PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/video/', PostViewSet.as_view({'get': 'get_video'}), name='post-video'),
    path('posts/<int:pk>/image/', PostViewSet.as_view({'get': 'get_image'}), name='post-image'),
]

