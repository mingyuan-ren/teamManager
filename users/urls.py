from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('add/', views.AddMemberClassView.as_view(), name='add'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]