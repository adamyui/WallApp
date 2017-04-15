from django import forms
from .models import Places
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import os
import audiotools


class PostForm(forms.ModelForm):
	def clean_audio(self):
		file = self.cleaned_data.get('sound',False)

		f = audiotools.open(file)
		try:
			result = f.verify()
		except audiotools.InvalidFile:
			print("invalid")
		else:
			print('valid')
	# def clean_sound(self):
	# 	file= self.cleaned_data.get('sound', False)
	# 	if file:
	# 		if file._size > 4*1024*1024:
	# 			raise ValidationError('Audio file too large(>4mb)')
	# 		if not file.content_type in ['audio/mpeg', 'audio/mp4','audio/wav', 'audio/ogg', 'audio/basic', 'audio/vorbis', 'audio/mp3']:
	# 			raise ValidationError('Content type incorrect')
	# 		if not os.path.splitext(file.name)[1] in ['.mp3', '.wav', '.ogg']:
	# 			raise ValidationError('Wrong extension')
	# 		return file
	class Meta:
		model = Places
		fields = [

			'title',
			'longitude',
			'latitude',
			'sound',
			
		]


# class InputLocForm(forms.Form):
# 	# current_longitude = forms.FloatField()
# 	# current_latitude = forms.FloatField()

# 	class Meta:
# 	model = Places
# 	fields = [
# 			'longitude',
# 			'latitude',

			
			
# 		]


















	

# Create your models here.
