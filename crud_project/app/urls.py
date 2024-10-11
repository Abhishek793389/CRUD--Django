from django.urls import path
from . import views


urlpatterns = [
    path('', views.master, name='master'),
    path('show/', views.show_table, name='home'),
    path('add/', views.employee_data, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    
   

   
]
