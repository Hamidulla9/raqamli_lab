from django.contrib import admin
from .models import Yangilik, Loyiha, Hodim, Taklif, Takliflarimiz, Boglanish


@admin.register(Yangilik)
class YangilikAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'description_uz', 'description_en', 'image',]


@admin.register(Loyiha)
class LoyihaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'description_uz', 'description_en', 'image', 'link', 'github_link', 'star',]


@admin.register(Hodim)
class HodimAdmin(admin.ModelAdmin):
    list_display = ('ism', 'yonalish', 'created_at', 'updated_at',)
    search_fields = ('ism',)
    fields = ['ism', 'yonalish', 'description_uz', 'description_en', 'image',]


@admin.register(Takliflarimiz)
class TakliflarimizAdmin(admin.ModelAdmin):
    fields = ['takliflar',]


@admin.register(Boglanish)
class BoglanishAdmin(admin.ModelAdmin):
    list_display = ('telefon', 'gmail', 'created_at', 'updated_at',)
    search_fields = ('telefon',)
    fields = ['xarita', 'description_uz', 'description_en', 'telefon', 'gmail', 'telegram_link', 'instagram_link',
              'facebook_link',]
