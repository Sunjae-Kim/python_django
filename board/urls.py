from django.urls import path
from . import views

# App 이름을 설정해준다.
app_name = 'board'

urlpatterns = [
    path('index/', views.index),  # DOMAIN/board/index
    path('greeting/<str:name>/<str:role>', views.greeting),  # DOMAIN/board/greeting/jason

    # Create
    # /articles/new => html (작성하는 화면)
    # /articles/create => DB new record
    path('articles/new', views.new),
    path('articles/create', views.create),

    # Read
    # /articles => html (all articles)
    # /articles/1 => html (article with 1)
    path('articles', views.all_list),
    # path('articles')

    # Update
    # /articles/1/edit => html (1 article 을 수정하는 화면)
    # /articles/1/update => DB update article with 1

    # Delete
    # /articles/1/delete => DB delete article with 1
]
