from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
	return render(request, 'main.html',{})

def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['비트코인','이더리움']
		})


def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        return_str = return_json_str['content']
 
        return JsonResponse({
                'message': {
                        'text': "you type "+return_str+"!"
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['1','2']
                }
        })