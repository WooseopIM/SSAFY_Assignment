from django.shortcuts import render

# Create your views here.

def push(request):
    return render(request,'push.html')

def pull(request):
    result = request.GET.get('push')
    context = {
        'result': result,
    }
    return render(request, 'pull.html', context)
