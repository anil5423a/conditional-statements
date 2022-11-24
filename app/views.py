from django.shortcuts import render

# Create your views here.


def condition(request):
    d={'a':10556,'b':80,'c':300}
    return render(request,'condition.html',context=d)