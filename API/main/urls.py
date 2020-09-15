from django.conf.urls import url, include
from django.urls import path
from .views import (
    UserCreate, UserLogin, UserUpdate, ChangePassword, UserDataViewSet, ProjectViewSet, PageViewSet,
    AssetView, BlockViewSet, LogicViewSet, OrderViewSet
)

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'main'

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'userdata', UserDataViewSet)
#router.register(r'projects', ProjectViewSet)
#router.register(r'pages', PageViewSet)
#router.register(r'assets', AssetViewSet)
router.register(r'blocks', BlockViewSet)
router.register(r'logic', LogicViewSet)

project_list = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',  # ? put method used initially
    'patch': 'partial_update',
    'delete': 'destroy',
})

page_list = PageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

page_detail = PageViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',  # ? put method used initially
    'patch': 'partial_update',
    'delete': 'destroy',
})

schema_view = get_schema_view(
    openapi.Info(
        title="Pipelines API",
        default_version='v1',
        x_logo={
            "url": "http://via.placeholder.com/350x250/78c5d6/fff/image1.jpg",
            "backgroundColor": "#FFFFFF",
            "altText": "Pipelines Logo",
            "href": "#",
        },
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(
            cache_timeout=0
        ),
        name='schema-json'
    ),
    url(
        r'^swagger/$',
        schema_view.with_ui(
            'swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    url(
        r'^redoc/$',
        schema_view.with_ui(
            'redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('register/', UserCreate.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name="login"),
    path('users/update/', UserUpdate.as_view(), name="user-update"),
    path('users/password/', ChangePassword.as_view(), name="change-password"),
    path('pages/<uuid:project>/', page_list, name="page-list"),
    path('page/<uuid:pk>/', page_detail, name="page-detail"),
    path('projects/', project_list, name="project-list"),
    path('projects/<uuid:pk>/', project_detail, name="project-detail"),
    path('assets/', AssetView.as_view(), name="asset-upload"),
]
