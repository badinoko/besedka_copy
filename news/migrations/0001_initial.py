# Generated by Django 4.2.21 on 2025-05-27 21:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=100, unique=True, verbose_name="URL-слаг"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question_text",
                    models.CharField(max_length=300, verbose_name="Вопрос"),
                ),
                (
                    "multiple_choice",
                    models.BooleanField(
                        default=False, verbose_name="Множественный выбор"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
            ],
            options={
                "verbose_name": "Опрос",
                "verbose_name_plural": "Опросы",
            },
        ),
        migrations.CreateModel(
            name="PollChoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "choice_text",
                    models.CharField(max_length=200, verbose_name="Текст варианта"),
                ),
                (
                    "votes",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество голосов"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="choices",
                        to="news.poll",
                        verbose_name="Опрос",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вариант ответа",
                "verbose_name_plural": "Варианты ответов",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                (
                    "slug",
                    models.SlugField(
                        max_length=200, unique=True, verbose_name="URL-слаг"
                    ),
                ),
                ("content", models.TextField(verbose_name="Содержание")),
                (
                    "excerpt",
                    models.TextField(
                        blank=True, max_length=300, verbose_name="Краткое описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="news/images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "post_type",
                    models.CharField(
                        choices=[
                            ("article", "Статья"),
                            ("video_link", "Видео-ссылка"),
                            ("poll", "Опрос"),
                        ],
                        default="article",
                        max_length=20,
                        verbose_name="Тип поста",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(blank=True, verbose_name="Ссылка на видео"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Черновик"), ("published", "Опубликовано")],
                        default="draft",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "is_pinned",
                    models.BooleanField(default=False, verbose_name="Закреплен"),
                ),
                (
                    "published_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата публикации"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "ordering": ["-is_pinned", "-published_at", "-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Название"
                    ),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="URL-слаг")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="PostView",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_address", models.GenericIPAddressField(verbose_name="IP-адрес")),
                (
                    "session_key",
                    models.CharField(
                        blank=True, max_length=40, verbose_name="Ключ сессии"
                    ),
                ),
                (
                    "viewed_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время просмотра"
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_views",
                        to="news.post",
                        verbose_name="Пост",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Просмотр поста",
                "verbose_name_plural": "Просмотры постов",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, to="news.tag", verbose_name="Теги"
            ),
        ),
        migrations.CreateModel(
            name="PollVote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "voted_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время голосования"
                    ),
                ),
                (
                    "choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.pollchoice",
                        verbose_name="Выбранный вариант",
                    ),
                ),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="news.poll",
                        verbose_name="Опрос",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Голос в опросе",
                "verbose_name_plural": "Голоса в опросах",
            },
        ),
        migrations.AddField(
            model_name="poll",
            name="post",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poll",
                to="news.post",
                verbose_name="Пост",
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="Содержание",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "is_edited",
                    models.BooleanField(default=False, verbose_name="Отредактирован"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="news.comment",
                        verbose_name="Родительский комментарий",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="news.post",
                        verbose_name="Пост",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Reaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reaction_type",
                    models.CharField(
                        choices=[
                            ("like", "👍"),
                            ("dislike", "👎"),
                            ("love", "❤️"),
                            ("laugh", "😂"),
                            ("wow", "😮"),
                            ("sad", "😢"),
                            ("angry", "😠"),
                        ],
                        max_length=10,
                        verbose_name="Тип реакции",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reactions",
                        to="news.comment",
                        verbose_name="Комментарий",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reactions",
                        to="news.post",
                        verbose_name="Пост",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Реакция",
                "verbose_name_plural": "Реакции",
                "indexes": [
                    models.Index(
                        fields=["post", "reaction_type"],
                        name="news_reacti_post_id_16a7ab_idx",
                    ),
                    models.Index(
                        fields=["comment", "reaction_type"],
                        name="news_reacti_comment_42ef0a_idx",
                    ),
                ],
            },
        ),
        migrations.AddConstraint(
            model_name="reaction",
            constraint=models.UniqueConstraint(
                condition=models.Q(("post__isnull", False)),
                fields=("post", "user"),
                name="unique_post_reaction_per_user",
            ),
        ),
        migrations.AddConstraint(
            model_name="reaction",
            constraint=models.UniqueConstraint(
                condition=models.Q(("comment__isnull", False)),
                fields=("comment", "user"),
                name="unique_comment_reaction_per_user",
            ),
        ),
        migrations.AddIndex(
            model_name="postview",
            index=models.Index(
                fields=["post", "user"], name="news_postvi_post_id_fb20ca_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="postview",
            index=models.Index(
                fields=["post", "ip_address", "session_key"],
                name="news_postvi_post_id_527d79_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["status", "published_at"], name="news_post_status_29dd9a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["is_pinned", "published_at"],
                name="news_post_is_pinn_73930a_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["category", "status"], name="news_post_categor_da046a_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pollvote",
            unique_together={("poll", "user", "choice")},
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["post", "created_at"], name="news_commen_post_id_f46bf4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["parent"], name="news_commen_parent__f18116_idx"
            ),
        ),
    ]
