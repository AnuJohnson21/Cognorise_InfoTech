from django.urls import path
from .views import*
from django.contrib import admin


urlpatterns=[

    path('main', main),
    path('home', home),
    path('login', login),
    path('signup', signup),
    path('add_todo', add_todo),
    path('log_out', log_out),
    path('delete_todo<int:id>', delete_todo),
    path('change_status<int:id>/<str:status>', change_todo),
]