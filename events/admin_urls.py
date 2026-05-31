from django.urls import path
from . import admin_views

urlpatterns = [
    path('', admin_views.dashboard, name='admin_dashboard'),
    path('events/', admin_views.event_list, name='admin_event_list'),
    path('events/add/', admin_views.event_add, name='admin_event_add'),
    path('events/<int:pk>/edit/', admin_views.event_edit, name='admin_event_edit'),
    path('events/<int:pk>/delete/', admin_views.event_delete, name='admin_event_delete'),
    path('categories/', admin_views.category_list, name='admin_category_list'),
    path('categories/add/', admin_views.category_add, name='admin_category_add'),
    path('categories/<int:pk>/delete/', admin_views.category_delete, name='admin_category_delete'),
    path('registrations/', admin_views.registration_list, name='admin_registration_list'),
    path('registrations/<int:pk>/', admin_views.registration_detail, name='admin_registration_detail'),
    path('registrations/<int:pk>/delete/', admin_views.registration_delete, name='admin_registration_delete'),
]
