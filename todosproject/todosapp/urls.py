
from django.urls import path, include

from .import views

urlpatterns = [
    path('',views.Todo,name='Todo'),
    path('delete/<int:taskid>/',views.Delete,name='delete'),
    path('edit/<int:id>/',views.Edit,name='edit'),
]
