# from django.shortcuts import get_object_or_404

from rest_framework import viewsets
# from rest_framework.exceptions import PermissionDenied

from .serializers import GroupSerializer, PostSerializer  #CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#    def perform_create(self, serializer):
#        serializer.save(author=self.request.user)

#    def perform_update(self, serializer):
#        if serializer.instance.author != self.request.user:
#            raise PermissionDenied('Изменение чужого контента запрещено!')
#        super(PostViewSet, self).perform_update(serializer)

#    def perform_destroy(self, instance):
#        if instance.author != self.request.user:
#            raise PermissionDenied('Удаление чужого контента запрещено!')
#        super(PostViewSet, self).perform_destroy(instance)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer