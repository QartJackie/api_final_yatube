from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (PostSerializer, CommentSerializer,
                             GroupSerializer, FollowSerializer)
from posts.models import Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly, )

    def perform_create(self, serializer):
        """Переопределение функции создания для добавления поста."""
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с комментариями."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        """Функция получения поста."""
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        """Переопределение queryset функции."""
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """Переопределение функции создания для добавления комментария"""
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для работы с группами (только чтение)."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с подписками."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def get_queryset(self):
        """Переопределение queryset функции."""
        return Follow.objects.select_related(
            'following').filter(user=self.request.user)

    def perform_create(self, serializer):
        """Переопределение функции создания для подписок."""
        serializer.save(user=self.request.user)
