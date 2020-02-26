from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# , PLAN_CHOICES, ASSET_TYPE_CHOICES
from .models import Order, UserData, Project, Page, Asset, Block, Logic


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write-only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, required=True)

    class Meta:
        model = UserData
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, required=True)

    class Meta:
        model = Project
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, required=True)

    class Meta:
        model = Page
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, required=True)

    class Meta:
        model = Asset
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, required=True)

    class Meta:
        model = Block
        fields = '__all__'


class LogicSerializers(serializers.ModelDurationField):
    project = ProjectSerializer(many=True, required=True)

    class Meta:
        model = Logic
        fields = '__all__'