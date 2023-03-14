from django.urls import path
from ToDo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_confirm_delete, name='task_confirm_delete'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete')

]

