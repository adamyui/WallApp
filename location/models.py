from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point



from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from constrainedfilefield.fields import ConstrainedFileField

import magic

from .validators import MimetypeValidator

class Places(models.Model):

	title= models.CharField(max_length=100)
	latitude= models.FloatField(null= True, blank=True,)
	longitude= models.FloatField(null= True, blank=True,) 
	location = models.PointField(null= True, srid=4326,default= Point(27,-38))
	objects = models.GeoManager()
	sound= ConstrainedFileField(max_upload_size= 4194304,)
	prefered_radius = models.IntegerField(default=5, help_text="in kilometers")
	rating= GenericRelation(Rating, related_query_name='foos')
	usersave= models.CharField(max_length=100)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.latitude and self.longitude:
			self.location = Point(self.longitude, self.latitude)
		
		super(Places,self).save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id': self.id})

	# def clean_file(self):
	# 	file = self.cleaned_data.get("sound", False)
	# 	filetype = magic.from_buffer(file.read())
	# 	if not "audio/mpeg" in filetype:
	# 		raise ValidationError("File is not XML.")
	# 	return file







	

































	


