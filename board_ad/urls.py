from django.urls import path
from . import views

# App 이름을 설정해준다.
app_name = 'board_ad'

urlpatterns = [
    # Read
    path('', views.posting_list, name='posting_list'),  # DOMAIN/articles/
    path('<int:id>', views.posting_detail, name='posting_detail'),  # DOMAIN/articles/4/
]
