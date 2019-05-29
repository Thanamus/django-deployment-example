# from django.conf.urls import path, url
from django.urls import path, include
from users_app import views


#Template urls!
app_name = 'users_app'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/', views.user_login,name='user_login'),
]
