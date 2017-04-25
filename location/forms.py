from django import forms
from .models import Places
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import magic

from .validators import MimetypeValidator

import os
# import audiotools


class PostForm(forms.ModelForm):
	# file= forms.FileField(
	# 	allow_empty_file=False,
	# 	validators=[MimetypeValidator('audio/mpeg')],
	# 	help_text= "Upload a ogg file"
	# 	)



	class Meta:
		model = Places
		fields = [

			'title',
			'longitude',
			'latitude',
			'sound',
			
		]





	def clean_audio_file(self, form):
		file = self.clean_sound.get('sound')
		

		if file:
			if _size > 4*1024*1024:
				raise ValidationError("Audio file too large ( > 4mb )")
			if not file.content_type in ["audio/mpeg","audio/wav"]:
				raise ValidationError("Content-Type is not mpeg")
			if not os.path.splitext(file.name)[1] in [".mp3",".wav"]:
				raise ValidationError("Doesn't have proper extension")
				return file
			else:
				raise ValidationError("Couldn't read uploaded file")


	# upload_file = forms.FileField(validators=[validate_file_infection])


	# def clean_audio(self):
	# 	file = self.cleaned_data.get('sound')
		
	# 	import audiotools
	# 	f = audiotools.open(file)
	# 	try:
	# 		result = f.verify()
	# 	except audiotools.InvalidFile:
	# 		print("invalid")
	# 	else:
	# 		print('valid')
	# 	return file























	

# Create your models here.
