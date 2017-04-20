from django.shortcuts import render, get_object_or_404,redirect
from django.views import View, generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.db.models import F
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from .models import Places
from .forms import PostForm

# import audiotools


#CRUD
@login_required(login_url='/accounts/login/')
def post_create(request):
	form= PostForm(request.POST or None, request.FILES or None)


	if form.is_valid():
		
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Created')
		return HttpResponseRedirect('/')

	
	context= {
		'form': form,
	}
	return render(request, 'location/post_form.html',context,)

def post_detail(request,id):
	instance= get_object_or_404(Places, id=id)
	context= {
		'title': instance.title,
		'instance': instance,
	}
	return render(request,'location/post_detail.html',context)


def post_update(request,id=None):
	instance= get_object_or_404(Places, id=id)
	form= PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():

		instance= form.save(commit=False)
		instance.save()
		messages.success(request,'Saved')
		#success
		return HttpResponseRedirect(instance.get_absolute_url())

	context= {
		'title': instance.title,
		'instance': instance,
		'form': form,
	}
	return render(request, 'location/post_form.html', context)

def post_delete(request, id=None):
	instance= get_object_or_404(Places, id=id)
	instance.delete()
	messages.success(request, 'Success')
	return redirect('posts:list')

def fetch_places(request):
	finder_location = Point(-83,33)

	nearby= Places.objects.filter(
		location__distance_lte=(
			finder_location,
			D(km=40))).distance(finder_location).order_by('distance')[:10]
	context= {
		'object_listboy': nearby,
		'title': 'wall',

	}
	return render(request, 'location/wall.html', context)


def fetch_places_loc(request):
	lat= request.GET['latitude']
	lon= request.GET['longitude']
	finder_location = Point(float(lon),float(lat))
	
	nearby= Places.objects.filter(
		location__distance_lte=(
			finder_location,
			D(km=40))).distance(finder_location).order_by('distance')[:10]
	context= {
		'object_listboy': nearby,
		'title': 'wall',

	}
	return render(request, 'location/wall.html', context)















