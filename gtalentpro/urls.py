from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    # candidate
    path('add_profile/', views.add_profile),
    path('find_jobs/', views.find_jobs),
    path('find_internships/', views.find_internships),
    path('recommended_jobs/', views.recommended_jobs),

    # job
    path('add_job/', views.add_job),
    path('find_talent/', views.find_talent),

    # login, registration, session
    path('login/', views.signin),
    path('logout/', views.signout),
    path('signup/', views.signup),
]