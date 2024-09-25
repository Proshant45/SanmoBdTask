from itertools import product
from lib2to3.fixes.fix_input import context
from django.contrib.auth import login
from .forms import AdminRegistrationForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Frontend Views

def product_list(request):
    under_200 = Product.objects.filter(price__lt=200)
    over_200 = Product.objects.filter(price__gte=200)
    context = {
        'under_200': under_200,
        'over_200': over_200,
    }
    return render(request, 'products/product_list.html', context)
def all_product(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'products/all_product.html' ,context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

# Admin CRUD Views

@login_required
def admin_product_list(request):
    products = Product.objects.all()
    return render(request, 'products/admin_product_list.html', {'products': products})

@login_required
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Create Product'})

@login_required
def admin_product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Update Product'})

@login_required
def admin_product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('admin_product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after registration (optional)
            login(request, user)
            return redirect('product_list')
    else:
        form = AdminRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
