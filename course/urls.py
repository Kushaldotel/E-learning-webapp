# elearning_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),

    path('', views.index, name='index'),
    path('teacher', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_courses/', views.view_courses, name='view_courses'),
]



urlpatterns += [
    # ... your existing URL patterns ...
    path('courses_list/', views.courses_list, name='courses_list'),
    path('course_detail/<int:pk>/', views.course_detail, name='course_detail'),
]
