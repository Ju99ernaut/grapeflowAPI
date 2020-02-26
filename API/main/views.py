#from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order, UserData, Project, Page, Asset, Block, Logic
from .serializers import (
    UserSerializer, OrderSerializer, UserDataSerializer, ProjectSerializer, PageSerializer,
    AssetSerializer, BlockSerializer, LogicSerializers
)
from rest_framework import viewsets


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class LogicViewSet(viewsets.ModelViewSet):
    queryset = Logic.objects.all()
    serializer_class = LogicSerializers
