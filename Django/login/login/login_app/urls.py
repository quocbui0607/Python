from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexClass.as_view(), name='índex'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('user-view/', views.UserView.as_view(), name='user_view'),
    path('view-pro/', views.viewProduct, name='view_pro'),
    path('add-post/', views.AddPost.as_view(), name='add_post')
]
