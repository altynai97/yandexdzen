from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Comment, Post, Category


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    video_url = serializers.HyperlinkedIdentityField(view_name='post-video', format='html')
    image_url = serializers.HyperlinkedIdentityField(view_name='post-image', format='html')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
