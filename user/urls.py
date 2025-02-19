from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('doctor/', views.index, name='doctor'),
    path('patient/', views.index, name='patient'),
]
