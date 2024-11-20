from rest_framework import viewsets
from .models import Yangilik, Loyiha, Hodim, Taklif, Takliflarimiz, Boglanish
from .serializers import YangilikSerializer, LoyihaSerializer, HodimSerializer, \
    TaklifSerializer, TakliflarimizSerializer, BoglanishSerializer


class YangilikViewSet(viewsets.ModelViewSet):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikSerializer


class LoyihaViewSet(viewsets.ModelViewSet):
    queryset = Loyiha.objects.all()
    serializer_class = LoyihaSerializer


class HodimViewSet(viewsets.ModelViewSet):
    queryset = Hodim.objects.all()
    serializer_class = HodimSerializer


class TaklifViewSet(viewsets.ModelViewSet):
    queryset = Taklif.objects.all()
    serializer_class = TaklifSerializer


class TakliflarimizViewSet(viewsets.ModelViewSet):
    queryset = Takliflarimiz.objects.all()
    serializer_class = TakliflarimizSerializer


class BoglanishViewSet(viewsets.ModelViewSet):
    queryset = Boglanish.objects.all()
    serializer_class = BoglanishSerializer
