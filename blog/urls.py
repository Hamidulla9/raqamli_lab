from django.urls import path
from .views import (
    TaklifListView,
    taklifdetail,
    TakliflarimizListView,
    takliflarimizdetail,
    BoglanishListView,
    boglanishdetail,
)

urlpatterns = [
    path('takliflar/', TaklifListView.as_view()),
    path('takliflar/<int:pk>/', taklifdetail),

    path('takliflarimiz/', TakliflarimizListView.as_view()),
    path('takliflarimiz/<int:pk>/', takliflarimizdetail),

    path('boglanish/', BoglanishListView.as_view()),
    path('boglanish/<int:pk>/', boglanishdetail),
]
