from django.urls import path

from . import views

urlpatterns = [
	path('active/', views.RetrieveActiveUserAPIView.as_view()),
	path('create/', views.CreateUserAPIView.as_view()),
	path('<int:user_id>/', views.RetrieveUserAPIView.as_view()),
	path('all/', views.RetreiveUsersAPIView.as_view()),
]