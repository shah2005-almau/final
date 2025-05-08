from rest_framework import viewsets, permissions, filters
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]  # 👈 Мына жолды қостық
    search_fields = ['title']  # 👈 Бұл өрістер бойынша іздейді

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
