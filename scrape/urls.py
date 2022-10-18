from django.urls import path

from . import views





urlpatterns = [
   
    path('', views.ScrapeView, name='scrape'),
    path('/score',views.ScoreView,name='score'),
    path('/ml_score',views.MLScoreView,name='ml_score'),

    #path('/postreq', views.ScrapePostReqView, name='scrapepostreq'),

    #path('submit/', views.SubmitView, name ='submit'),
 
]