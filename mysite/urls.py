from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def operations(request, ops, a, b):
  print('Getting Data')
  print('OPS:', ops)
  print('NUM1:', a)
  print('NUM2:', b)
  if ops== 'sum':
    res = a + b
    return JsonResponse({"result": res})
  elif ops == 'diff':
    res = abs(a-b)
    return JsonResponse({"result": res})
  elif ops== 'multiply':
    res = a*b
    return JsonResponse({"result": res})
  elif ops == 'divison':
    res = a/b
    return JsonResponse({"result": res})
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:ops>/<int:a>/<int:b>', operations)
]