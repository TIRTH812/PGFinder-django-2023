from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .forms import ProductForm

def getAllProducts(request):

    #select * from products
    products = Product.objects.all().values()
    #products = Product.objects.all().values_list('pName','pPrice','pQty')
    #products = Product.objects.all().values('pName','pPrice','pQty')

    #fetch single object
    #product =Product.objects.get(id=1)

    #price greater thn....
    #__ django orm lookups
    #products  = Product.objects.filter(pPrice__gte = 800).values()     # Greater than and equals to
    #products  = Product.objects.filter(pPrice__lte = 800).values()     # Lower than and equals to
    #products = Product.objects.filter(pName__startswith='i').values()  # Name starts with letter i
    #products = Product.objects.filter(pName__contains='p').values()    # Name which contains letter p
    #products = Product.objects.filter(pName__icontains='P').values()   # case insensitive
    
    #orderby
    #products = Product.objects.all().order_by('pName').values()        # Ascending Order
    #products = Product.objects.all().order_by('-pName').values()       # Descending Order

    print(products)     # print in console(CMD)
    return render(request,'product/allproducts.html',{'products':products})

def addProducts(request):

    #add product
    #productdict ={'pName':'mouse2','pPrice':100,'pQty':10,'pDesc':'mouse for laptop','pStatus':True,'pColor':'black'}
    product = Product(pName ="mouse pad",pPrice=100,pQty=10,pDes="mouse pad for laptop",pStatus=True,pColor="black")
    #product = Product(productdict)
    product.save()
    print("Product Added")
    return render(request,'product/addproducts.html')

def deleteProduct(request,id):
    #delete product
    #id = 1
    product = Product.objects.get(id=id)
    product.delete()

    return HttpResponse("Product Deleted")
    #return render(request,'product/deleteproduct.html')

def updateProduct(request,id):
    #update product
    #id = 1
    product = Product.objects.get(id=id)
    product.pName = "lenovo laptop"
    product.pPrice = 500000
    product.save()

    return HttpResponse("Product Updated")
    #return render(request,'product/updateproduct.html')

def addProductWithForm(request):

    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse("Product Added")    

    return render(request,'product/addproductwithform.html',{'form':form})    

    # Second Method
    # if request.method == "POST":
    #     pName = request.POST['pName']
