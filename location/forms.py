from django import forms
from .models import Places
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

import os
import audiotools


class PostForm(forms.ModelForm):

	def clean_audio_file(self, sound):
		file = self.cleaned_data.get('sound')
		

		if file:
			if file._size > 4*1024*1024:
				raise ValidationError("Audio file too large ( > 4mb )")
			if not file.content-type in ["audio/mpeg","audio/wav"]:
				raise ValidationError("Content-Type is not mpeg")
			if not os.path.splitext(file.name)[1] in [".mp3",".wav"]:
				raise ValidationError("Doesn't have proper extension")
	             # Here we need to now to read the file and see if it's actually 
	             # a valid audio file. I don't know what the best library is to 
	             # to do this
	             # if not some_lib.is_audio(file.content):
	             #       raise ValidationError("Not a valid audio file")
				return file
			else:
				raise ValidationError("Couldn't read uploaded file")


	# upload_file = forms.FileField(validators=[validate_file_infection])


	def clean_audio(self):
		file = self.cleaned_data.get('sound')
		f = audiotools.open(file)
		import audiotools
		try:
			result = f.verify()
		except audiotools.InvalidFile:
			print("invalid")
		else:
			print('valid')
		return file

	class Meta:
		model = Places
		fields = [

			'title',
			'longitude',
			'latitude',
			'sound',
			
		]
























	

# Create your models here.
