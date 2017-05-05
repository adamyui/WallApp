from django import forms
from .models import Places
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import magic
import os


class PostForm(forms.ModelForm):

	def clean_sound(self):
		file = self.cleaned_data.get('sound',False,)
		# filetype = magic.from_buffer(file.read(1024))
		# mime = magic.Magic(mime=True)

		
		if file:
			if file.size > 4*1024*1024:
				raise ValidationError("Audio file too large ( > 4mb )")
			if not file.content_type in ["audio/mpeg","audio/mp3",]:
				raise ValidationError("Wrong file type, make sure to use mp3/wav")
			if not os.path.splitext(file.name)[1] in [".mp3",]:
				raise ValidationError("Doesn't have proper extension")
			
			# if not "audio/mp3" in filetype:
			# 	raise ValidationError("File is not mp3.")
			
			return file
		else:
			raise ValidationError("Couldn't read uploaded file")


	class Meta:
		model = Places
		fields = [
		'usersave',
		'title',
		'longitude',
		'latitude',
		'sound',
			
		]




























		




























