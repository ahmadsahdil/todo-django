from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from .models import todo



def index(request):
    items = todo.objects.order_by('-id')
    return render(request, 'todo/index.html', {'items':items})

def done(request):
    items = todo.objects.filter(status=True).order_by('-id')
    return render(request, 'todo/index.html', {'items':items})

def pending(request):
    items = todo.objects.filter(status=False).order_by('-id')
    return render(request, 'todo/index.html', {'items':items})

def delete_all(request):
    todo.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))

def create(request):
    try:
        title = request.POST['namatitle']
        Todo = todo(title=title)
        Todo.save()
        return HttpResponseRedirect(reverse('index'))
    except Exception:
        return HttpResponseRedirect(reverse('index'))


def update(request, id):
    try:
        Todo = todo.objects.get(id=id)
        Todo.status = not Todo.status
        Todo.save()
        return HttpResponseRedirect(reverse('index'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    try:
        Todo = todo.objects.get(id=id)
        Todo.delete()
        return HttpResponseRedirect(reverse('index'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('index'))
    
