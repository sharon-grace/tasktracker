from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),

]
