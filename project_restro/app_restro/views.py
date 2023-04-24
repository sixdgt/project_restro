from django.shortcuts import render
from .forms import CategoryCreateForm, MenuCreateForm

# Create your views here.
def menu_index(request):
    return render(request, 'menus/index.html')

def menu_add(request):
    menu_form = MenuCreateForm()
    context = {
        "form": menu_form,
        "title": "Menu Create Form"
    }
    return render(request, 'menus/create.html', context)

def menu_edit(request):
    return render(request, 'menus/edit.html')

def menu_show(request):
    return render(request, 'menus/show.html')

# category views
def category_create(request):
    form = CategoryCreateForm()
    context = {
        "form": form,
        "title": "Category Create Form"
    }
    return render(request, "menus/add_category.html", context)