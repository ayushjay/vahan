from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.ScrapeView, name='scrape'),
    #path('submit/', views.SubmitView, name ='submit'),
 
]