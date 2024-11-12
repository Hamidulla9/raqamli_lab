from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from .models import Yangilik, Loyiha, Hodim, Taklif, Takliflarimiz, Boglanish
from .pagination import ResultsSetPagination
from .serializers import YangilikSerializer, HodimSerializer, LoyihaSerializer, TaklifSerializer, \
    TakliflarimizSerializer, BoglanishSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class YangilikListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = YangilikSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Yangilik.objects.all().order_by('title')


@api_view(['GET'])
def yangilikdetail(request, pk):
    yangilik = get_object_or_404(Yangilik, pk=pk)
    serializer = YangilikSerializer(yangilik, context={'request': request})
    return Response(serializer.data)


class HodimListView(ListAPIView):
    search_fields = ['ism']
    filter_backends = (filters.SearchFilter,)
    serializer_class = HodimSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Hodim.objects.all().order_by('ism')


@api_view(['GET'])
def hodimdetail(request, pk):
    hodim = get_object_or_404(Hodim, pk=pk)
    serializer = HodimSerializer(hodim, context={'request': request})
    return Response(serializer.data)


class LoyihaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LoyihaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Loyiha.objects.all().order_by('title')


@api_view(['GET'])
def loyihadetail(request, pk):
    loyiha = get_object_or_404(Loyiha, pk=pk)
    serializer = LoyihaSerializer(loyiha, context={'request': request})
    return Response(serializer.data)


class TaklifListView(ListAPIView):
    serializer_class = TaklifSerializer

    def get_queryset(self):
        return Taklif.objects.all().order_by('created_at')


@api_view(['GET'])
def taklifdetail(request, pk):
    taklif = get_object_or_404(Taklif, pk=pk)
    serializer = TaklifSerializer(taklif, context={'request': request})
    return Response(serializer.data)


class TakliflarimizListView(ListAPIView):
    serializer_class = TakliflarimizSerializer

    def get_queryset(self):
        return Takliflarimiz.objects.all().order_by('id')


@api_view(['GET'])
def takliflarimizdetail(request, pk):
    takliflarimiz = get_object_or_404(Takliflarimiz, pk=pk)
    serializer = TakliflarimizSerializer(takliflarimiz, context={'request': request})
    return Response(serializer.data)


class BoglanishListView(ListAPIView):
    serializer_class = BoglanishSerializer

    def get_queryset(self):
        return Boglanish.objects.all().order_by('created_at')


@api_view(['GET'])
def boglanishdetail(request, pk):
    boglanish = get_object_or_404(Boglanish, pk=pk)
    serializer = BoglanishSerializer(boglanish, context={'request': request})
    return Response(serializer.data)
