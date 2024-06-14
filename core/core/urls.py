from unicodedata import name
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from authentication import views 

 
# Defining URL patterns
urlpatterns = [
                path('', home, name="home"),                              #landing page
                path("admin/", admin.site.urls, name='admin'),               #admin interface
                path('login/', login_page, name='login_page'),              #login page
                path('register/', register_page, name='register'),          # registration page
                path('tasks/', views.task_list, name='task_list'),                 #url routes for tasks
                path('task_create/', views.task_create, name='task_create'),
                path('task_update/<int:pk>/', views.task_update, name='task_update'),
                path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
                path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
                path('tickets/', views.ticket_list, name='ticket_list'),               #url routes for tickets
                path('ticket_delete/<int:pk>/', views.ticket_delete, name='ticket_delete'),
                path('ticket_create/', views.ticket_create, name='ticket_create'),
                path('ticket_update/<int:pk>/', views.ticket_update, name='ticket_update') ]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
