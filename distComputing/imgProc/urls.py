from django.urls import path

from . import views

urlpatterns = [
    path('facialRecog/', views.facialRecog),
    path('crowdCnt/', views.crowdCnt)
]
