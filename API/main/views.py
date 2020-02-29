#from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order, UserData, Project, Page, Asset, Block, Logic
from .serializers import (
    UserSerializer, OrderSerializer, UserDataSerializer, ProjectSerializer, PageSerializer,
    AssetSerializer, BlockSerializer, LogicSerializer
)
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied


class UserCreate(generics.CreateAPIView):
    """
    Create and return new user instance given valid data
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class OrderCreate(generics.CreateAPIView):
    """
    Create and return new order instance given valid data
    """
    serializer_class = OrderSerializer


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List the authenticated user's orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        List the authenticated user's orders
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Detailed view of a single order
        """
        order = Order.objects.get(pk=self.kwargs["pk"])
        if not request.user == order.user:
            raise PermissionDenied("You can not access this project.")
        return super().retrieve(request, *args, **kwargs)


class UserDataViewSet(viewsets.ModelViewSet):
    """
    Creates and returns user data instance given valid data
    """
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def get_queryset(self):
        """
        List the authenticated user's user data
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Detailed view of user data
        """
        user_data = UserData.objects.get(pk=self.kwargs["pk"])
        if not request.user == user_data.user:
            raise PermissionDenied("You can not access this project.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated user data instance given valid data
        """
        user_data = UserData.objects.get(pk=self.kwargs["pk"])
        if not request.user == user_data.user:
            raise PermissionDenied("You can not access this project.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a user data instance
        """
        user_data = UserData.objects.get(pk=self.kwargs["pk"])
        if not request.user == user_data.user:
            raise PermissionDenied("You can not access this project.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Not available
        """
        pass


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Creates and returns project instance given valid data
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        List the authenticated user's projects
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Detailed view of a single project created by the authenticated user
        """
        project = Project.objects.get(pk=self.kwargs["pk"])
        if not request.user == project.user:
            raise PermissionDenied("You can not access this project.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated project given valid data
        """
        project = Project.objects.get(pk=self.kwargs["pk"])
        if not request.user == project.user:
            raise PermissionDenied("You can not access this project.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a project instance
        """
        project = Project.objects.get(pk=self.kwargs["pk"])
        if not request.user == project.user:
            raise PermissionDenied("You can not access this project.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a project instance
        """
        project = Project.objects.get(pk=self.kwargs["pk"])
        if not request.user == project.user:
            raise PermissionDenied("You can not delete this project.")
        return super().destroy(request, *args, **kwargs)


class PageViewSet(viewsets.ModelViewSet):
    """
    Creates and returns page instance given valid data
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self):
        """
        List the pages in a given project 
        """
        queryset = self.queryset
        query_set = queryset.filter(project__user=self.request.user)
        return query_set

    # def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of a page instance
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.project__user:
            raise PermissionDenied("You can not access this project.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated page instance given valid data
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.project__user:
            raise PermissionDenied("You can not access this project.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a page instance
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.project__user:
            raise PermissionDenied("You can not access this project.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a page instance
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.project__user:
            raise PermissionDenied("You can not delete this project.")
        return super().destroy(request, *args, **kwargs)


class AssetViewSet(viewsets.ModelViewSet):
    """
    Creates and returns asset instance given valid data
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get_queryset(self):
        """
        List assets in a given project
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of an asset instance
        """
        asset = Asset.objects.get(pk=self.kwargs["pk"])
        if not request.user == asset.user:
            raise PermissionDenied("You can not access this asset.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated asset instance given valid data
        """
        asset = Asset.objects.get(pk=self.kwargs["pk"])
        if not request.user == asset.user:
            raise PermissionDenied("You can not access this asset.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update an asset instance
        """
        asset = Asset.objects.get(pk=self.kwargs["pk"])
        if not request.user == asset.user:
            raise PermissionDenied("You can not access this asset.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete an asset instance
        """
        asset = Asset.objects.get(pk=self.kwargs["pk"])
        if not request.user == asset.user:
            raise PermissionDenied("You can not delete this asset.")
        return super().destroy(request, *args, **kwargs)


class BlockViewSet(viewsets.ModelViewSet):
    """
    Creates and returns block instance given valid data
    """
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def get_queryset(self):
        """
        List all custom blocks in a given project
        """
        queryset = self.queryset
        query_set = queryset.filter(project__user=self.request.user)
        return query_set

    # def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of a block instance
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.project__user:
            raise PermissionDenied("You can not access this block.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated block instance given valid data
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.project__user:
            raise PermissionDenied("You can not access this block.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update an block instance
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.project__user:
            raise PermissionDenied("You can not access this block.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a block instance
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.project__user:
            raise PermissionDenied("You can not delete this block.")
        return super().destroy(request, *args, **kwargs)


class LogicViewSet(viewsets.ModelViewSet):
    """
    Creates and returns logic instance given valid data
    """
    queryset = Logic.objects.all()
    serializer_class = LogicSerializer

    def get_queryset(self):
        """
        List all custom logic in a given project
        """
        queryset = self.queryset
        query_set = queryset.filter(project__user=self.request.user)
        return query_set

    # def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of a logic instance
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.project__user:
            raise PermissionDenied("You can not access this logic.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated logic instance given valid data
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.project__user:
            raise PermissionDenied("You can not access this logic.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a logic instance
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.project__user:
            raise PermissionDenied("You can not access this logic.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a logic instance
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.project__user:
            raise PermissionDenied("You can not delete this logic.")
        return super().destroy(request, *args, **kwargs)
