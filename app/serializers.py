from rest_framework import serializers
from .models import Post, Coordinates, Comment

class Coordinates(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'altitude']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'text', 'coords', 'created']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text', 'created']