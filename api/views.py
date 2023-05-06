from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAuthorOrAllowAny
from .serializers import CommentSerializer, PostSerializer, CategorySerializer
from .models import Comment, Post, Category


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    @action(detail=True, methods=['get'])
    def get_video(self, request, pk=None):
        post = self.get_object()
        video_url = post.video.url
        return Response({'url': video_url})

    @action(detail=True, methods=['get'])
    def get_image(self, request, pk=None):
        post = self.get_object()
        image_url = post.image.url
        return Response({'image_url': image_url})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
