from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('people_list/', views.people_list, name='people_list'),
 

]