from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', login_required(views.home), name='home'),
    path('admin-home/', login_required(views.admin_home), name='admin_home'),
    path('admin-tasks/', login_required(views.admin_tasks), name='admin_tasks'),
    path('admin-projects/', login_required(views.admin_projects), name='admin_projects'),
    path('register/', views.manual_register, name='register'),
    path('login/', views.login_view, name='manual_login'),
    path('profile/', views.profile_page, name='profile_page'),
    path('tasks/', views.tasks, name='tasks'),
    path('projects/', views.projects, name='projects'),
    path('report/', views.report, name='report'),
    path('admin-report/', views.admin_report, name='admin_report'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/update/', views.update_project_status, name='update_project_status'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path("api/users/", views.get_users, name="get_users"),
    path('get_users/', views.get_users, name='get_users'),
    path('projects/<int:project_id>/save_excalidraw_data/', views.save_excalidraw_data, name="save_excalidraw_data"),
    path('projects/<int:project_id>/get_excalidraw_data/', views.get_excalidraw_data, name="get_excalidraw_data"),
    path('social-login-redirect/', views.social_login_redirect, name='social_login_redirect'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/update/', views.update_task_status, name='update_task_status'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/complete/', views.mark_task_complete, name='mark_task_complete'),
    path('notifications/', login_required(views.notifications), name="notifications"),
    path('admin_notifications/', login_required(views.admin_notifications), name="admin_notifications"),
    path('schedule_meeting/', views.schedule_meeting, name='schedule_meeting'),
]