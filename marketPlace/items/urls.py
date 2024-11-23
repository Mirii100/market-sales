from django.urls import path
from  . import views

app_name='items'
urlpatterns = [
    path('',views.browse,name='items'),
    path('new/',views.new,name='new'),
    path('<int:pk>/',views.item_detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),

]