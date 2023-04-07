from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def view_list(request: HttpRequest):
    items = Item.objects.all()
    return render(request, "list.html", {'items': items})

def new_list(request: HttpRequest):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect('/list/the-only-list-in-the-world/')
