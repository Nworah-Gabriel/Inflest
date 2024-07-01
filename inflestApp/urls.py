from django.urls import path
from . import views

urlpatterns = [
  
   
     path('analysis3/', views.analysis_view, name='analysis_view'),
]
