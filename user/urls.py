from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('doctor/', views.index, name='doctor'),
    path('patient/', views.index, name='patient'),
    path('blogs/', views.blogs, name='blogs'),
	path('blogs/<int:id>/', views.readBlog, name='blog'),
	path('selfblogs/', views.selfblogs, name='selfblog'),
	path('selfblogs/<int:id>/', views.readBlog, name='blog'),
]
