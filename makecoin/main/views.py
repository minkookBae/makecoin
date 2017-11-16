from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
 
def keyboard(request):
 
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['1','2']
                })
 
@csrf_exempt
def message(request):
        return_str = "이게 답이다"
        return JsonResponse({
                'message': {
                        'text': "you type "+return_str+"!"
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['1','2']
                }
        })
