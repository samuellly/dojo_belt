from django.shortcuts import render,redirect
from .models import Product
from ..login_app.models import Person
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.


def index(request):
    if 'user_id' in request.session:
        user= Person.objects.get(id=request.session['user_id'])
        context={
            'data': user,

            'items': Product.objects.all().filter(group=user),

            'users': Product.objects.all().exclude(group=user)

        }
        return render(request, 'wish_app/index.html', context)
    else:
        return redirect(reverse('login:index'))

def display(request, item_id):
    item = Product.objects.get(id=item_id)
    context = {
        'items': item,
        'users': item.group.all()
    }
    return render(request, 'wish_app/display.html', context)

def create(request):
    return render(request, 'wish_app/create.html')

def process(request):
    if request.method == 'POST':
        user = Person.objects.get(id=request.session['user_id'])
        result= Product.objects.addProduct(request.POST, user)
        if result[0] == True:
            messages.success(request,result[1])
            return redirect(reverse('wishlist:index'))
        else:
            for error in result[1]:
                messages.error(request, error)
            return redirect(reverse('wishlist:create'))

def join(request, item_id):
    user = Person.objects.get(id=request.session['user_id'])
    result= Product.objects.joinProduct(item_id, user)
    messages.success(request, "Item moved  to your list ")
    return redirect(reverse('wishlist:index'))


def delete(request, item_id):
    Product.objects.get(id= item_id).delete()
    messages.success(request, "Item Deleted ")
    return redirect(reverse('wishlist:index'))

def remove(request, item_id):
    user = Person.objects.get(id=request.session['user_id'])
    item = Product.objects.get(id= item_id)
    item.group.remove(user)
    messages.success(request, "Itme removed from your table")
    return redirect(reverse('wishlist:index'))

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "You have been successfully logged out")
        return redirect(reverse('login:login'))
