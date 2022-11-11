from . import views
from django.urls import path
app_name = 'store'
urlpatterns=[
    path('',views.index,name='index'),
    path('science', views.science, name='science'),
   path('cscience', views.cscience, name='cscience'),
   path('biology', views.biology, name='biology'),
   path('history', views.history, name='history'),
   path('commerce', views.commerce, name='commerce'),

]