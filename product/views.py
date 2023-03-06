from django.shortcuts import render, redirect
from .models import Product,Category
from django.http import HttpResponse
from .forms import ProductForm,CategoryForm

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

    # return HttpResponse("Product Deleted")
    #return render(request,'product/deleteproduct.html')
    return redirect('getproducts')

def updateProduct(request,id):
    #update product
    #id = 1
    product = Product.objects.get(id=id)
    product.pName = "lenovo laptop"
    product.pPrice = 500000
    product.save()

    return HttpResponse("Product Updated")
    #return render(request,'product/updateproduct.html')

def getProductDetail(request,id):
    product = Product.objects.get(id=id)    
    return render(request,'product/productdetail.html',{'product':product})

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

def updateProductWithForm(request,id):

    product = Product.objects.get(id=id)
    form = ProductForm()

    print("post.....")
    form = ProductForm(request.POST or None,instance=product)    
    if form.is_valid():
        form.save()
        return redirect('getproducts')  

    return render(request,'product/updateproductwithform.html',{'form':form})  

# -------------------------------------------------------------------------------------------------------

def addCategory(request):
    form = CategoryForm()
    if request.method =="POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('getcategories')

    return render(request,'product/addcategory.html',{'form':form})    

def getAllCategories(request):
    categories = Category.objects.all().values()
    return render(request,'product/allcategories.html',{'categories':categories})

def deleteCategory(request,id):

    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect('getcategories')

def updateCat(request,id):
    cat = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None,instance=cat)
    if form.is_valid():
        cat.save()
        return redirect('getcategories')

    return render(request,'product/updatecategory.html',{'form':form})