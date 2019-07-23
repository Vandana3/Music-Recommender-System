from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
	path('popular/<int:user_id>/', views.popular_music, name='popular_music'),
	path('cf/<int:user_id>/', views.cf, name='cf'),
	path('genre/<int:user_id>/', views.genre, name='genre'),
	path('login/', views.login, name = 'login'),
	path('signup/', views.signup, name = 'signup'),
]