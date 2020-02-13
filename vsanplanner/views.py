from django.shortcuts import render
from .models import Clusters

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse


class IndexView(generic.ListView):
	context_object_name='cluster_list'
	template_name = 'vsanplanner/index.html'

	def get_queryset(self):
		return Clusters.objects.all()


class ClusterEntry(CreateView):
    model = Clusters
    fields=['CustomerName','OndiskOver','NumDG','NumCapDisks','SSDSize','NumNodes','FTM','Clusterid','RawCap','SpbmCap']

   
class ClusterUpdate(UpdateView):
	model = Clusters
	fields=['CustomerName','OndiskOver','NumDG','NumCapDisks','SSDSize','NumNodes','FTM','Clusterid','RawCap','SpbmCap']

class ClusterDelete(DeleteView):
	model = Clusters
	success_url = reverse_lazy('vsanplanner:index')
