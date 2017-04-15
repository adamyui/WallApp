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

import audiotools




# def clean_audio(self):
	
# 	file= 

# 	f = audiotools.open(sound)
# 	try:
# 		result = f.verify()
# 	except audiotools.InvalidFile:
# 		print("invalid")
# 	else:
# 		print('valid')






#CRUD
@login_required(login_url='/accounts/login/')
def post_create(request):
	form= PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():


		clean_audio(request.FILES['sound'])


		instance = form.save(commit=False)
		instance.save()
		
		messages.success(request, 'Successfully Created')
	
	context= {
		'form': form,
	}
	return render(request, 'location/post_form.html',context)

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



@login_required(login_url='/accounts/login/')
def post_list(request):
	queryset= Places.objects.all()
	# candidates= queryset.filter()

	context= {
		'object_list': queryset,
		'title': 'wall',

	}
	return render(request, 'location/wall.html', context)










#GEOSTUFF



def fetch_places(request):
	current_longitude = 38
	current_latitude = -29


	
	finder_location = Point(float(37),float(-29))

	

	nearby= Places.objects.filter(
		location__distance_lte=(
			finder_location,
			D(km=500))).distance(finder_location).order_by('distance')


	context= {
		'object_listboy': nearby,
		'title': 'wall',

	}
	return render(request, 'location/wall.html', context)








# def location_input(request):
# 	form= InputLocForm()
# 	if request.method == 'POST':
# 		form= InputLocForm(data=request.POST)
# 		if form.is_valid():
# 			m= form.cleaned_data['current_longitude', 'current_latitude']
# 			return m 


# 	context= {

# 		'form' : form,

# 	}
# 	return render(request, 'location/post_form.html', context)









