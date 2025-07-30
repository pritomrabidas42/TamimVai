from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'product/product_list.html', {
        'products': products,
        'query': query
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})
