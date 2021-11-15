from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tasks/', views.taskIndex, name="tasks-index"),
    path('tasks/<str:pk>/', views.taskShow, name="tasks-show"),
    path('tasks/<str:pk>/update', views.taskUpdate, name="tasks-update"),
    path('tasks/<str:pk>/delete', views.taskDelete, name="tasks-delete"),
    path('tasks/create', views.taskCreate, name="tasks-create"),
]
