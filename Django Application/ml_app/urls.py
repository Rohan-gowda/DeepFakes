"""ml_app URL Configuration
"""
from django.urls import path
from . import views

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    # Authentication URLs
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    
    # Main App URLs
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('predict/', views.predict_page, name='predict'),
    path('cuda_full/', views.cuda_full, name='cuda_full'),
]
