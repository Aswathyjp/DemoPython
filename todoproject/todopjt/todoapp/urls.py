from django.urls import path
from . import views
urlpatterns = [
     path("",views.add,name='add'),
    # path("detailpage",views.detail,name="detail")
     path('delete/<int:taskid>/',views.delete,name='delete'),
     path('update/<int:id>/',views.update,name='update'),
     path('cbviewhome/',views.Tasklistview.as_view(),name='cbviewhome'),
     path('cvbdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cvbdetail'),
     path('cvbupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cvbupdate'),
     path('cvbdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cvbdelete')
]