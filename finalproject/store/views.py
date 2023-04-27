from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.user
        order, created = Order.objects.get_or_create(costumer=customer, complete=False)
        items = OrderItem.objects.all()
    else:
        order = Order.objects.get_or_create(complete=False)
        items = []

    context = {"items": items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.user
        order, created = Order.objects.get_or_create(costumer=customer, complete=False)
        items = OrderItem.objects.all()
    else:
        order = Order.objects.get_or_create(complete=False)
        items = []


    context = {"items": items, 'order': order}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    customer = request.user.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(costumer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def payed(request):
    if request.user.is_authenticated:
        customer = request.user.user
        order, created = Order.objects.get_or_create(costumer=customer, complete=False)
        items = OrderItem.objects.all()
    else:
        order = Order.objects.get_or_create(complete=False)
        items = []
    context = {"items": items, 'order': order}
    return render(request, 'store/placedorder.html', context)