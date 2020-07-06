from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.RetrieveCarsAPIView.as_view()),
	path('create/', views.CreateCarAPIView.as_view()),
	path('<int:car_id>/', views.RetrieveUpdateCarAPIView.as_view()),
	path('assing/', views.AssingCarOwnerAPIView.as_view()),
]