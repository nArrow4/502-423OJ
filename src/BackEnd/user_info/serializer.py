from django.contrib.auth.models import User
from rest_framework import serializers


# 在文章列表序列化中使用
class UserDescSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'date_joined',
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)