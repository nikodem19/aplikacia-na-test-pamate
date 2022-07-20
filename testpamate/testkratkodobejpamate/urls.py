
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='testpamate-home'),
    path('about/', views.about, name='testpamate-about'),
    path('testkid/', views.testkid, name='testpamate-testkid'),
    path('teststudent/', views.teststudent, name='testpamate-teststudent'),
    path('testadult/', views.testadult, name='testpamate-testadult'),
    path('testsenior/', views.testsenior, name='testpamate-testsenior'),
    path('results/', views.results, name='testpamate-results'),
]
