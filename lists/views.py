from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        Item.objects.create(text=request.POST["item_text"])
        return redirect('/list/the-only-list-in-the-world/')
    return render(request, 'home.html')

def view_list(request: HttpRequest):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
