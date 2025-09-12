from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

# all products in json format
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

# all products in xml format
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

# show json product by id
def show_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(
        serializers.serialize("json", [product]),
        content_type="application/json"
    )

# show xml product by id
def show_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(
        serializers.serialize("xml", [product]),
        content_type="application/xml"
    )

def show_main(request):
    context = {
        'app_name': 'Goalified',
        'name': '2406408224 - Nadine Aisyah Putri Maharani',
        'class_name': 'PBP F'
    }
    return render(request, 'main/main.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "main/product_list.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        "product": product
    }
    return render(request, "main/product_detail.html", context)

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:product_list")
    else:
        form = ProductForm()
    return render(request, "main/add_product.html", {"form": form})