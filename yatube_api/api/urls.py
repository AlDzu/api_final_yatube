from django.urls import include, path

from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = SimpleRouter()

router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='post_id'),
router.register('v1/follow', FollowViewSet, basename='user_id')

urlpatterns = [
    path('', include(router.urls)),
]
