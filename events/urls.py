from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('explore/', views.explore, name='explore'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/register/', views.register_event, name='register_event'),
    path('event/<int:pk>/bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('bookmarks/', views.my_bookmarks, name='my_bookmarks'),
]
