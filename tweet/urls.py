from django.urls import path,include
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path("post/new",views.PostCreateView.as_view(),name='post-create'),

 #   path('',views.LikeHome.as_view(), name='like-home'),
#    path('accounts/login', include('allauth.urls'),name='accounts-login'),
]
