from django.shortcuts import render
from .application import auto_capture

def index(request):
	return render(request, 'auto_capture_app/index.html')

def get_capture_query(request):
	if request.method == "GET":
		auto_capture.get_capture(request.GET.get('target_url'))
		return render(request, 'auto_capture_app/complete.html')