from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('thesis',views.thesis,name='thesis'),
    path('info',views.info,name='info'),
    path('index1',views.index1,name='index1'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]
