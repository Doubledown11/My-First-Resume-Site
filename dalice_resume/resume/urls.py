from django.urls import path, include 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


app_name = 'resume'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('experiences/', views.experiences, name='experiences'),
    path('skills/', views.skills, name='skills'),
    path('certifications/', views.certifications, name='certifications'),
    path('educations/', views.educations, name='educations'),
    path('volunteers/', views.volunteers, name='volunteers'),


    # Paths for Blog section: 
    path('blogs/', views.blogs, name='blogs'),
    path('blogs(admin)/', views.blogs_admin, name='blogs(admin)'),
    path('blog/<int:blog_ID>/', views.blog, name='blog'),
    path('blog(admin)/<int:blog_ID>/', views.blog, name='blog(admin)'),

    path('new_blog/', views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_ID>/', views.edit_blog, name='edit_blog'),
    path('admin_blogs/', views.admin_blogs, name='admin_blogs'),  
    path('delete_blog/<int:blog_ID>/', views.delete_blog, name='delete_blog'),

    path('aboutme/', views.aboutme, name='aboutme'),


    # Path for users app:
    path('users/', include('users.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)