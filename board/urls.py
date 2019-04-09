from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),  # DOMAIN/board_ad/index
    path('greeting/<str:name>/<str:role>', views.greeting),  # DOMAIN/board_ad/greeting/jason

    # Create
    # /articles/new => html (작성하는 화면)
    # /articles/create => DB new record
    path('articles/new/', views.article_new),
    path('articles/create/', views.article_create),

    # Read
    # /articles => html (all articles)
    # /articles/1 => html (article with 1)
    path('articles/', views.article_list),
    path('articles/<int:article_id>/', views.article_detail),

    # Update
    # /articles/1/edit => html (1 article 을 수정하는 화면)
    # /articles/1/update => DB update article with 1
    path('articles/<int:article_id>/edit/', views.article_edit),
    path('articles/<int:article_id>/update/', views.article_update),

    # Delete
    # /articles/1/delete => DB delete article with 1
    path('articles/<int:article_id>/delete/', views.article_delete),
]
