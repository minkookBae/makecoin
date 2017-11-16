
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request, 'main.html',{})

def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['비트코인','이더리움']
		})