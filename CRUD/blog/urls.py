from django.urls import path

from .views import *
from . import views

app_name="blog"
urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('layout/', views.layout, name='layout'),
    path('blog/<int:blog_id>/comment', views.detail, name="detail"),
    path('blog/home/', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogform, name='newblog'),
    path('<int:blog_id>/edit/', views.edit, name='edit'),
    path('<int:blog_id>/remove/',views.remove, name='remove'),
    path('<int:blog_id>/<int:comment_id>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('<int:blog_id>/<int:comment_id>/remove_comment/', views.remove_comment, name='remove_comment'),
]