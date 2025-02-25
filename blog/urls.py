from django.urls import path
from . import views
from user.views import index

urlpatterns = [
    path('bdfadsf/', index, name='index'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('blog/<int:id>/<int:blogId>/', views.loadDraft, name='blog'),
    path('saveDraft/', views.savedraft, name='draft'),
    path('publish/', views.publish, name='publish'),
    path('delete/', views.delete, name='delete'),
]
