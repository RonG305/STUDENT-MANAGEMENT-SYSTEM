from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student/', views.create_student, name='create_student'),
    path('update_student/<str:pk>', views.update_student, name='update_student'),
    path('delete_student/<str:pk>', views.delete_student, name='delete_student')
]
