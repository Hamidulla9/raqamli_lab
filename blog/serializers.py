from rest_framework import serializers
from .models import Yangilik, Loyiha, Hodim, Taklif, Takliflarimiz, Boglanish


class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = ['id', 'image', 'title', 'description', 'created_at', 'updated_at']


class LoyihaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyiha
        fields = ['id', 'image', 'title', 'link', 'github_link', 'star', 'description', 'created_at', 'updated_at']


class HodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hodim
        fields = ['id', 'ism', 'description', 'yonalish', 'image', 'created_at', 'updated_at']


class TaklifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taklif
        fields = ['id', 'image', 'description', 'created_at', 'updated_at']


class TakliflarimizSerializer(serializers.ModelSerializer):
    takliflar = TaklifSerializer(many=True)

    class Meta:
        model = Takliflarimiz
        fields = ['id', 'takliflar']


class BoglanishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boglanish
        fields = ['id', 'longitud', 'latitude', 'description', 'telefon', 'gmail', 'telegram_link', 'instagram_link', 'facebook_link',
                  'created_at', 'updated_at']
