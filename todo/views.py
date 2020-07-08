from django.shortcuts import render, redirect


# Create your views here
def todo_list(request):
    return render(request, 'todo/list.html')
