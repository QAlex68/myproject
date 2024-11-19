from django.contrib import admin
from .models import Author, Article, Comment, CoinFlip


# Register your models here.

@admin.action(description="Сменить имя на None")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(name='None')


# можно через декоратор так короче
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['name', 'last_name', 'email', 'bio', 'birthday']
#     ordering = ['last_name']
#     ...


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'bio', 'birthday']
    ordering = ['last_name']
    list_filter = ['email', 'birthday']
    actions = [reset_quantity]
    search_fields = ['bio']
    search_help_text = 'Поиск по полю Биография(bio)'

    """Отдельный автор. Изменение отображения в админке"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['birthday']  # Нельзя редактировать
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Фамилия и биография автора',
                'fields': ['last_name', 'bio'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email'],

            }
        ),
        (
            'Дата рождения',
            {
                'description': 'Дата рождения',
                'fields': ['birthday'],
            }
        ),
    ]


# myModels: list = [Author, Article, Comment, CoinFlip]
myModels: list = [Article, Comment, CoinFlip]
admin.site.register(myModels)
admin.site.register(Author, AuthorAdmin)

# admin.site.register(Author)
# admin.site.register(Article)
# admin.site.register(Comment)
# admin.site.register(CoinFlip)
