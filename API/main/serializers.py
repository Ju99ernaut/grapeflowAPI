from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
# , PLAN_CHOICES, ASSET_TYPE_CHOICES
from .models import Order, UserData, Project, Page, Asset, Block, Logic
from drf_extra_fields.fields import Base64ImageField


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

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


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def update(self, instance, validated_data):
        for (key,  value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint
    """
    old_password = serializers.CharField(
        max_length=128, write_only=True, required=True)
    new_password = serializers.CharField(
        max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _("Your old password is incorrect. Please try again")
            )
        return value

    def validate(self, data):
        validate_password(data['new_password'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        Token.objects.create(user=user)
        return user


class OrderSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=True, required=True)
    expires = serializers.ReadOnlyField()
    active = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user']


class UserDataSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=True, required=True)

    class Meta:
        model = UserData
        fields = '__all__'
        read_only_fields = ['user']


class ProjectSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=True, required=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['user', 'published']


class PageSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer(many=True, required=True)

    class Meta:
        model = Page
        fields = '__all__'
        read_only_fields = ['project']


class AssetSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=True, required=True)
    size = serializers.ReadOnlyField()

    class Meta:
        model = Asset
        fields = '__all__'
        read_only_fields = ['user']


class BlockSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer(many=True, required=True)
    preview = Base64ImageField()

    class Meta:
        model = Block
        fields = '__all__'
        read_only_fields = ['user']


class LogicSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer(many=True, required=True)

    class Meta:
        model = Logic
        fields = '__all__'
        read_only_fields = ['user']
