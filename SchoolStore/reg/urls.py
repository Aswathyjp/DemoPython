from . import views
from django.urls import path

app_name = 'reg'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('regform',views.regform,name='regform'),
    path('newform',views.newform,name='newform'),
    path('logout',views.logout,name='logout'),
    # path('display/<int:u_id>',views.display,name='display'),
    # # path('detail',views.detail,name='detail'),

]