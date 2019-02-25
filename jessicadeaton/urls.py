from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('posts', views.post_list, name='post_list'),
	path('now', views.now, name='now'),
	path('about', views.about, name='about'),



]