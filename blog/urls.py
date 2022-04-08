from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(
    ), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('homepage/', views.Homepage.as_view(), name='homepage'),
    path('findus/', views.Findus.as_view(), name='findus'),
    path('trainers/', views.Trainers.as_view(), name='trainers'),
    path('pilates/', views.Pilates.as_view(), name='pilates'),
    path('spin/', views.Spin.as_view(), name='spin'),
    path('circuits/', views.Circuits.as_view(), name='circuits'),
]
