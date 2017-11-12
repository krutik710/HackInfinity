from django.conf.urls import url
from django.contrib import admin
from farm_assist import views

urlpatterns = [
    url(r'^login/', views.login_site),
    url(r'^register/', views.register),
    url(r'^farmer_homepage/', views.farmer_homepage),
    url(r'^seeds/', views.seeds),
    url(r'^fert/', views.fertilizer),
    url(r'^discuss/', views.discuss),

]