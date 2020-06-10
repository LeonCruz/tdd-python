from django.shortcuts import render, redirect
from lists.models import Item, List
from django.core.exceptions import ValidationError


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)

    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = 'Você não pode ter um item vazio em uma lista'
        return render(request, 'home.html', {'error': error})

    return redirect(f'/lists/{list_.id}/')