from django.urls import path
from . import views

app_name='blog'
urlpatterns =[

    path('', views.main, name="main"),
    path('new/',views.new, name="new"),
    path('blog/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>/', views.edit, name='edit'), # detail/정수 형태로 url을 설계
    path('delete/<int:article_id>/',views.delete, name="delete"),
    path('comment_delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('comment_edit/<int:comment_id>/', views.comment_edit, name="comment_edit"),
    # int : article_id -> path converter 
]