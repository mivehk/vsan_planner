"""sddcdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
from django.conf.urls import url , include

from vsanplanner import views

app_name='vsanplanner'

urlpatterns = [
    url(r'^$', views.IndexView.as_view() , name='index'),
    url(r'^Clusters/entry/$', views.ClusterEntry.as_view(), name='cluster-entry'),
    url(r'^Clusters/(?P<pk>[0-9]+)/$' , views.ClusterUpdate.as_view(), name='cluster-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete$' , views.ClusterDelete.as_view(), name='cluster-delete'),
]
