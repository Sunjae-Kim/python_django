from django.urls import path
from . import views

# App 이름을 설정해준다.
app_name = 'board_ad'

urlpatterns = [
    # Posting
    # Create
    path('new/', views.posting_new, name="posting_new"),

    # Read
    path('', views.posting_list, name='posting_list'),  # DOMAIN/articles/
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),  # DOMAIN/articles/4/

    # Update
    path('edit/<int:posting_id>/', views.posting_edit, name='posting_edit'),

    # Delete
    path('delete/<int:posting_id>/', views.posting_delete, name='posting_delete'),

    # Comment
    # Create
    path('<int:posting_id>/comment/new', views.comment_new, name='comment_new'),

    # Delete
    path('<int:posting_id>/comment/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),
]
