from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userdata', views.UserDataViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'pages', views.PageViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'blocks', views.BlockViewSet)
router.register(r'logic', views.LogicViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
