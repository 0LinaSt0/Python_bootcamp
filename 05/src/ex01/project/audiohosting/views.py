from django.http import JsonResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from typing import Dict, Any

class Audio(TemplateView):
	template_name = "audio/index.html"


	def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
		content = super().get_context_data(**kwargs)
		content["tracks"] = self.get_tracks()
		return content


	def get_tracks(self):
		return {
			name: default_storage.url(name) for name in default_storage.listdir("")[1]
		}.items()

class Upload(TemplateView):
	def post(self, request):
		file = request.FILES.get('inputFile')
		if file:
			self.save_file(file)
		return HttpResponseRedirect("/")


	def save_file(self, file):
		if default_storage.exists(file.name):
			default_storage.delete(file.name)
		default_storage.save(file.name, file)


	def get(self, request, *args, **kwargs):
		files = [
			name for name in default_storage.listdir("")[1]
		]
		return JsonResponse(dict(audios=files))
