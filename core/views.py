from django.shortcuts import render,get_object_or_404
from .models import Item,Category

def index(request):
    items = Item.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'items':items,
        'categories':categories,
    })

def detail(request,id):
    items = Item.objects.get(pk=id)
    # 浏览量+1
    items.total_views+=1
    items.save(update_fields=['total_views'])
    return render(request,'core/detail.html',{
        'items':items,
    })


def cet(request):
    items = Item.objects.filter(category_id=4)
    return render(request,'core/cet.html',{
        'items':items,
    })

def neccs(request):
    items = Item.objects.filter(category_id=6)
    return render(request,'core/neccs.html',{
        'items':items,
    })

def tv(request):
    items = Item.objects.filter(category_id=3)

    return render(request,'core/tv.html',{
        'items':items,
    })

def movie(request):
    items = Item.objects.filter(category_id=5)
    return render(request,'core/movie.html',{
        'items':items,
    })

def bl(request):
    items = Item.objects.filter(category_id=8)
    return render(request,'core/bl.html',{
        'items':items,
    })