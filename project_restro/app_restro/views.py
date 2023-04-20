from django.shortcuts import render

# Create your views here.
def menu_index(request):
    return render(request, 'menus/index.html')

def menu_add(request):
    return render(request, 'menus/create.html')

def menu_edit(request):
    return render(request, 'menus/edit.html')

def menu_show(request):
    return render(request, 'menus/show.html')