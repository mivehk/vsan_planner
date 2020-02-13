from django.db import models
from decimal import Decimal
from django.db.models import F

# Create your models here.

from django.urls import reverse
from modelchoices import Choices 

"""class FTM_Choices(Choices):
	ErasureCode5 = (0.75,'FTM5-PFTT1')
	ErasureCode6 = (0.67,'FTM6-PFTT2')
	PFTT0 = (1.0,'PFTT0')
	PFTT1 = (0.50,'PFTT1')
	PFTT2 = (0.33,'PFTT2')
	PFTT3 = (0.25,'PFTT3')"""

class Clusters(models.Model):
	# .67 & .33 caused those two choices to show invalid , since 2/3 & 1/3 needed float numbers so had to change FTM field datatype to float number
	FTM_choices = [(1.00,'PFTT0'),(0.50,'PFTT1'),(0.333,'PFTT2'),(0.25,'PFTT3'),(0.75,'FTM5-PFTT1'),(0.67,'FTM6-PFTT2')]
	CustomerName = models.CharField(max_length=128)
	OndiskOver = models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True,default=Decimal('0.98'))
	NumDG = models.IntegerField()
	NumCapDisks = models.IntegerField()
	SSDSize = models.IntegerField()
	NumNodes = models.IntegerField()
	FTM = models.FloatField(choices=FTM_choices,blank=False)
	Clusterid = models.AutoField(primary_key=True)
	RawCap = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
	SpbmCap = models.DecimalField(max_digits=10,decimal_places=2,blank=True ,null=True)

	def get_absolute_url(self):
		return reverse('vsanplanner:index')

	def RawCapacity(self,*args,**kwargs):
		rc=Clusters.objects.get(Clusterid=self.Clusterid)
		rc.RawCap = F('SSDSize')*F('NumCapDisks')*F('NumDG')*F('NumNodes')*0.98
		rc.save()
		rc.refresh_from_db()
		return rc.RawCap 

	def SpbmCapacity(self,*args,**kwargs):
		spbmc=Clusters.objects.get(Clusterid=self.Clusterid)
		spbmc.SpbmCap = F('SSDSize')*F('NumCapDisks')*F('NumDG')*F('NumNodes')*F('FTM')*0.98
		spbmc.save()
		spbmc.refresh_from_db()
		return spbmc.SpbmCap			

				    #super().save(*args,**kwargs)
				    #return self.RawCap

	"""def RawCapacity(SSDSize, OndiskOver, NumCapDisks, NumDG, NumNodes):
				    RC = self.SSDSize*self.OndiskOver*self.NumCapDisks*self.NumDG*self.NumNodes
				    return RC
	def SpbmCapacity(RawCapacity ,FTM):
		return RawCapacity*FTM"""