from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from django.urls import path, include
from .views import PostViewSet
from comments.views import CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

nested_router = NestedSimpleRouter(router, r'posts', lookup='post')
nested_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
