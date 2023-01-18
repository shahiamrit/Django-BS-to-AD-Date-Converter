from django.urls import path
from .import views

urlpatterns = [
    path('dc', views.neview),
    path('', views.con),
    path('crop/<str:pk>/', views.conId),
    path('upload/', views.UploadView.as_view()),
    path('db', views.userDb),
    path ('tmpfile', views.tempFileView),
    path('tmpfile/<str:token>', views.tempFileDownloadView, name='file_download')
]
