from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
 
def keyboard(request):
 
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['하창권','배민국','박희원']

                })
 
@csrf_exempt
def message(request):
        return_str = "멍청이 개발자"
        return JsonResponse({
                'message': {
                        'text': "아직까지는 "+return_str+"!"
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['하창권','배민국','박희원']
                }
        })

