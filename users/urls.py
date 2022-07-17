from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('add/', views.AddMemberClassView.as_view(), name='add'),
    path('edit/<int:pk>/',views.EditMemberClassView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteMemberClassView.as_view(), name='delete'),
]