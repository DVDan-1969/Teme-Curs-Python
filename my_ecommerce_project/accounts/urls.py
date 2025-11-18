
from django.urls import path
from . import views
from .views import  delete_user, admin_view
app_name = 'accounts'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('admin-users/', admin_view, name='admin_view'),
]


