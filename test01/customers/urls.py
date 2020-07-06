from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateCustomerAPIView.as_view()),
    path('list/', views.ListCustomersAPIView.as_view()),
]