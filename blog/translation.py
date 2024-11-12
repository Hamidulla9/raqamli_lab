from .models import Yangilik, Loyiha, Hodim, Taklif, Boglanish
from modeltranslation.translator import register, TranslationOptions


@register(Yangilik)
class YangilikTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Loyiha)
class LoyihaTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Hodim)
class HodimTranslationOptions(TranslationOptions):
    fields = ('description', 'yonalish')


@register(Taklif)
class TaklifTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Boglanish)
class BoglanishTranslationOptions(TranslationOptions):
    fields = ('description',)