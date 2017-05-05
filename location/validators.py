from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
import magic

class MimetypeValidator(object):
	def __init__(self, mimetypes):
		self.mimetypes = mimetypes
	def __call__(self, sound):
		try:
			mime = magic.from_buffer(sound.read(1024), mime=True)
			if mime not in self.mimetypes:
			
				raise ValidationError("wrong type")
		except AttributeError as e:
			raise ValidationError('wrong type')






