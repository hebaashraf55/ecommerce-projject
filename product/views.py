from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def product_list(request):
    product_list = Product.objects.all()
    
    paginator = Paginator(product_list, 4) 
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context = {'product_list': product_list}
    return render(request, 'Product/product_list.html', context )
    
      
       
def product_details(request, id):
    product_details = Product.objects.get(id=id)
    context = {'product_details' : product_details}
    return render(request, 'Product/product_details.html' , context)

