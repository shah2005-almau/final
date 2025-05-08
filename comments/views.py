from rest_framework import viewsets, permissions  # ✅ осылай болу керек

from .models import Comment
from .serializers import CommentSerializer
from posts.permissions import IsAuthorOrReadOnly  # 👈 рұқсатты сол жақтан аламыз

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Comment.objects.none()  # Swagger үшін бос queryset
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])
