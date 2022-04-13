from django.http import HttpResponse
from django.shortcuts import render
from . models import Places
from . models import Details

# Create your views here.
def demo(request):
    obj=Places.objects.all()
    obj1 = Details.objects.all()
    return render(request,"index.html",{'result':obj,'answer':obj1})



#def result(request):
 #   x = int(request.GET['num1'])
 #   y = int(request.GET['num2'])
 #  add = x + y
 #  mul = x * y
 # div = x / y
 #  return render(request, "result.html", {'a': add, 's': sub, 'm': mul, 'd': div})
