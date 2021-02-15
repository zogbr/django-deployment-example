from django.db import models

# Create your models here.
class User(User):
	title = forms.CharField(max_length=30)
	speciality = forms.CharField(max_length=255)
	phone1 = forms.CharField(max_length=30)
	phone2 = forms.CharField(max_length=30)
	phonemobile = forms.CharField(max_length=30)
	city = forms.CharField(max_length=50)

	class Meta(object):
		model = User
		fields('username', 'first_name', 'last_name', 'email', 'password', 'groups', 'is_active', 'is_superuser', )