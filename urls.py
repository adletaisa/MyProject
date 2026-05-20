from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_habit, name='add_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('toggle/<int:habit_id>/', views.toggle_habit, name='toggle_habit'),
]