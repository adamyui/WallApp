# Walkie-Talk

Walkie-Talk is a audio-sharing platform that allows you to listen to "sounds" posted in your area. It's intended for musicians, artists, and people who just need an anonymous creative outlet.

## Getting Started

-Visit walkie-talk.com. You'll see a list of audio players with sounds from the default location (Athens, GA)</br>
-Click the location on/off switch</br>
-Click the "listen" button</br>
-listen to the sounds of your fellow humans</br>

### Prerequisites

So this is technically a prerequisite: only mp3's under 4mb for uploads, please.

### Front end
<i>Found in: WallApp/location/templates/location/wall.html</i>

Luckily most popular browsers support the JavaScript function
```
navigator.geolocation.getCurrentPosition()
```
and that's pretty great news. There are some rules that might cause your browser to throw an error, including the fact that you cant request the users' location unless it's in a response to a users' action. Hence, the location on/off switch. I think it adds a little value for the users who like pressing buttons and switches (like me).

As far as the visual design, I tried to make it simple but got carried away with the CSS3 webkit animations. Sorry about that, animations are awesome.

### Form Validation
<i>Found in: WallApp/location/forms.py</i>

I used the Python package Python-Magic for form validation (Along with some JavaScript header/extension checking and some other server-side checking). Here's the essence of the forms' model:

```
class PostForm(forms.ModelForm):

	def clean_sound(self):
		file = self.cleaned_data.get('sound',False)
		mime = magic.from_buffer(file.read(), mime=True)
		print(mime)
		if not mime == 'audio/mpeg':
			raise forms.ValidationError('File must be mp3')
		else:
			return file
```

### Views.py
<i>Found in: WallApp/location/views.py</i>

I used GeoDjango to sort the audio objects, which proved especially handy when used with the postGIS database. Here's the view that displays the sounds once it grabs the users' location, with special thanks to the GeoDjango "D" query:
```
def fetch_places_loc(request):
	lat= request.GET['latitude']
	lon= request.GET['longitude']
	
	finder_location = Point(int(lon), int(lat))
	
	nearby= Places.objects.filter(
		location__distance_lte=(
			finder_location,
			D(km=40))).distance(finder_location).order_by('distance')[:10]
	context= {
		'object_listboy': nearby,
		'title': 'wall',

	}
	return render(request, 'location/wall.html', context)
```


I tried to list the most important bits of code that make this app work, but there are tons of other brain busting problems that I encountered that aren't listed here. Feel free to contact me with any questions, or if you're working on a similar app.

## Built With

* Django
* Python
* postgreSQL
* postGIS
* JavaScript
* HTML5
* CSS3


## Authors

* **Adam Mizell**

## License

This project is licensed under the MIT License 

## Acknowledgments
 Thanks to all my music/web development world friends!


