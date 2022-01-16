from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.throttling import AnonRateThrottle
from . import  models
import json

# Create your views here.
class FormView(View):
    throttle_classes = (AnonRateThrottle,)

    def get(self, request):
        return JsonResponse({'code': 0, 'message': 'Success!'})

    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name', '')
        phone = data.get('phone', '')
        email = data.get('email', '')
        company = data.get('company', '')
        need = data.get('need', '')
        form = models.Form(name=name, phone=phone, email=email, company=company, need=need)
        form.save()
        return JsonResponse({'code': 0, 'message': 'Success!'})