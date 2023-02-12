import base64
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator, ValidationError
from posts.models import Comment, Follow, Group, Post, User


class Base64ImageField(serializers.ImageField):
    """Кастомный сериализатор для декодирования картинок."""

    def to_internal_value(self, data):
        """Функция декодирования картинок."""
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор постов."""

    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        """Настройка взаимодействия с моделью."""
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        """Настройка взаимодействия с моделью."""
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Настройка взаимодействия с моделью."""
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        """Настройка взаимодействия с моделью."""
        fields = ('user', 'following')
        model = Follow
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого пользователя'
            ),
        )
        read_only_fields = ('user', 'following')

    def validate(self, data):
        """Функция-валидатор: запрещает подписку на себя."""
        if self.context['request'].user == data['following']:
            raise ValidationError('Подписка на себя невозможна.')
        return data
