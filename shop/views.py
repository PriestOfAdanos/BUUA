from .models import Product, Order
from .forms import NewBasket
from django.shortcuts import render, redirect


def orders_to_fulfil(request):
    orders = Order.objects.all()  #filter(picked_up=False)
    return render(request, 'list_of_orders.html', {'orders': orders})


def main_page(request):
    all_products = Product.objects.all()
    form = NewBasket
    return render(request, 'home.html', {'all_products': all_products})


def order_summary(request):
    if request.method == 'POST':
        form = NewBasket(request.POST)
        list_of_products = request.POST['product']
        if form.is_valid:
            form.products = Product.objects.filter(id_in=list_of_products)
            form.save()
            return redirect('progress_page.html')
