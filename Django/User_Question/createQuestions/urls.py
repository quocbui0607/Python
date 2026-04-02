from django.urls import path
from . import views

urlpatterns = [
    path('create-question/', views.createQuestion, name='createQuestion'),
    path('view-question/', views.viewQuestion, name='viewQuestion'),
    path('create-answer/', views.createAnswer, name='create_answer'),
    path('view-answer/', views.viewAnswer, name='view_answer'),
    path('upvote/', views.upvote, name='upvote'),
    path('downvote/',  views.downvote, name='downvote'),
    path('getToken/', views.getToken,name='token')

]