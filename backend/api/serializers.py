from rest_framework import serializers

from feed.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'content','numLikes', 'created',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user','post', 'content','numLikes', 'created',)
        model = Comment