#from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Order, UserData, Project, Page, Asset, Block, Logic
from .serializers import (
    UserCreateSerializer, UserUpdateSerializer, OrderSerializer, UserDataSerializer, ProjectSerializer, PageSerializer,
    AssetSerializer, BlockSerializer, LogicSerializer, ChangePasswordSerializer
)
from rest_framework.parsers import FileUploadParser
from rest_framework import views, generics, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied


class UserCreate(generics.CreateAPIView):
    """
    Create and return new user instance given valid data
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserCreateSerializer


class UserLogin(views.APIView):
    """
    Endpoint for logging in users
    """
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        # todo start the session for session authentication
        user = authenticate(username=username, password=password)
        if user:
            if hasattr(user, 'user_data'):
                uuid = user.user_data.uuid
            else:
                uuid = ""
            return Response({
                "user": UserCreateSerializer(user).data,
                "id": user.id,
                "userDataUuid": uuid,
                "token": user.auth_token.key
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(generics.UpdateAPIView):
    """
    An endpoint for updating user information
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def get_object(self):
        """
        Get the authenticated user
        """
        return self.request.user


class ChangePassword(generics.UpdateAPIView):
    """
    An endpoint for changing password
    """
    serializer_class = ChangePasswordSerializer


class OrderViewSet(viewsets.ModelViewSet):
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
        if self.request.user:
            serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Detailed view of a single order
        """
        order = Order.objects.get(pk=self.kwargs["pk"])
        if not request.user == order.user:
            raise PermissionDenied("You can not access this object.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update not available
        """
        pass

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update not available
        """
        pass

    def destroy(self, request, *args, **kwargs):
        """
        Delete not available
        """
        pass


class UserDataViewSet(viewsets.ModelViewSet):
    """
    List, create and return user data given valid data
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
        if self.request.user:
            serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Detailed view of user data
        """
        user_data = UserData.objects.get(pk=self.kwargs["pk"])
        if not request.user == user_data.user:
            raise PermissionDenied("You can not access this object.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated user data instance given valid data
        """
        user_data = UserData.objects.get(pk=self.kwargs["pk"])
        if not request.user == user_data.user:
            raise PermissionDenied("You can not access this object.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a user data instance
        """
        user_data = UserData.objects.get(pk=self.kwargs["pk"])
        if not request.user == user_data.user:
            raise PermissionDenied("You can not access this object.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete not available
        """
        pass


class ProjectViewSet(viewsets.ModelViewSet):
    """
    List, create and return projects given valid data
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
        if self.request.user:
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
    List, create and return pages given valid data
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self, *args, **kwargs):
        """
        List the pages in a given project 
        """
        queryset = self.queryset
        query_set = queryset.filter(
            project__user=self.request.user)
        # todo groupby project
        try:
            return query_set.filter(project=self.kwargs["project"])
        except KeyError:
            return query_set

    def perform_create(self, serializer, *args, **kwargs):
        try:
            serializer.save(
                project=Project.objects.get(uuid=self.kwargs["project"])
            )
        except KeyError:
            raise PermissionDenied("Unable to create page without project")

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of a page instance
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.getUser():
            raise PermissionDenied("You can not access this page.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated page instance given valid data
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.getUser():
            raise PermissionDenied("You can not access this page.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a page instance
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.getUser():
            raise PermissionDenied("You can not access this page.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a page instance
        """
        page = Page.objects.get(pk=self.kwargs["pk"])
        if not request.user == page.getUser():
            raise PermissionDenied("You can not delete this page.")
        return super().destroy(request, *args, **kwargs)


class AssetView(views.APIView):
    """
    Upload asset files
    """
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        if request.user:
            asset_serializer = AssetSerializer(data=request.data)
            if asset_serializer.is_valid():
                asset_serializer.save(user=request.user)
                return Response(asset_serializer.data, status=status.HTTP_201_CREATED)
            return Response(asset_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if request.user:
            assets = Asset.objects.filter(user=request.user)
            asset_serializer = AssetSerializer(assets, many=True)
            return Response(asset_serializer.data)


class BlockViewSet(viewsets.ModelViewSet):
    """
    List, create and return blocks given valid data
    """
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def get_queryset(self):
        """
        List all custom blocks in a given project
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        if self.request.user:
            serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of a block instance
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.user:
            raise PermissionDenied("You can not access this block.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated block instance given valid data
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.user:
            raise PermissionDenied("You can not access this block.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update an block instance
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.user:
            raise PermissionDenied("You can not access this block.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a block instance
        """
        block = Block.objects.get(pk=self.kwargs["pk"])
        if not request.user == block.user:
            raise PermissionDenied("You can not delete this block.")
        return super().destroy(request, *args, **kwargs)


class LogicViewSet(viewsets.ModelViewSet):
    """
    List, create and return logic given valid data
    """
    queryset = Logic.objects.all()
    serializer_class = LogicSerializer

    def get_queryset(self):
        """
        List all custom logic in a given project
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        if self.request.user:
            serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns detailed view of a logic instance
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.user:
            raise PermissionDenied("You can not access this logic.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update and return updated logic instance given valid data
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.user:
            raise PermissionDenied("You can not access this logic.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a logic instance
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.user:
            raise PermissionDenied("You can not access this logic.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Destroy/Delete a logic instance
        """
        logic = Logic.objects.get(pk=self.kwargs["pk"])
        if not request.user == logic.user:
            raise PermissionDenied("You can not delete this logic.")
        return super().destroy(request, *args, **kwargs)
