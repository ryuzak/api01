from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.BrandListAPIView.as_view()),
    path('create/', views.BrandCreateAPIView.as_view()),
]