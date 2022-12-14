from django.urls import path
from .views import Audio, Upload

urlpatterns = [
	path('', Audio.as_view()),
	path('upload/', Upload.as_view())
]