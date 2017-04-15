from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Places(models.Model):
	# # user = models.OneToOneField(User, on_delete=models.CASCADE)
	title= models.CharField(max_length=100)
	latitude= models.FloatField(null= True, blank=True)
	longitude= models.FloatField(null= True, blank=True) 
	location = models.PointField(null= True, srid=4326)
	objects = models.GeoManager()
	sound= models.FileField()
	prefered_radius = models.IntegerField(default=5, help_text="in kilometers")
	rating= models.IntegerField(default= 1)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.latitude and self.longitude:
			self.location = Point(self.longitude, self.latitude)
		
		super(Places,self).save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id': self.id})



	












	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Place.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	# 	instance.place.save()


# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	latitude= models.FloatField(null= True, blank=True)
# 	longitude= models.FloatField(null= True, blank=True) 
# 	location = models.PointField(null= True, srid=4326)
	
# 	def save(self, *args, **kwargs):
# 		if self.latitude and self.longitude:
# 			self.location = Profile(self.longitude, self.latitude)
		
# 		super(Profile,self).save(*args,**kwargs)










	# class Meta:
	# 	ordering = []
















	

# Create your models here.
