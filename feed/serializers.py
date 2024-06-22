from rest_framework import serializers
from django.contrib.auth.models import User

from feed.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "description", "created_at", "user", "can_delete"]

    def get_can_delete(self, obj):
        request = self.context.get("request")
        return obj.user == request.user
