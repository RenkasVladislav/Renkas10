from django.urls import path, include
from . import views
app_name = 'blog'
urlpatterns = [
 # post views
 path('', views.post_list, name='post_list'),
 path('<int:id>/', views.post_detail, name='post_detail'),
 path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]
