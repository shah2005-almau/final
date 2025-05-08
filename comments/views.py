from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer
from posts.permissions import IsAuthorOrReadOnly  # 👈 рұқсатты сол жақтан аламыз

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])
