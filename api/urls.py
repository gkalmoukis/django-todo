from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tasks/', views.taskIndex, name="tasks-index"),
    path('tasks/<str:pk>/', views.taskShow, name="task-show"),
]
