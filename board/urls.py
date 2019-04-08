from django.urls import path
from . import views

# App 이름을 설정해준다.
app_name = 'board'

urlpatterns = [
    path('index/', views.index),  # DOMAIN/board/index
    path('greeting/<str:name>/<str:role>', views.greeting),  # DOMAIN/board/greeting/jason
]
