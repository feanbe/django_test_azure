from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_list', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('csv', views.csv_test_export, name='csv'),
]