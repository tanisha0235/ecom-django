from django.shortcuts import render,HttpResponse
from ecomapp.models import Product,Product_Detail,Brand_Detail,Final_Detail,Conclude_Detail
from django.template import loader
from django.shortcuts import redirect

# Create your views here.
def pro_index(request):
    mdata=Product.objects.all()
    sdata={'mdata':mdata}
    return render(request,'ecomapp/index.html',sdata)
    
def product_detail(request,id):
    sqdata=Product.objects.get(pk=id)
    spdata=Product_Detail.objects.filter(pid=sqdata.pk)
    pdata={'spdata':spdata}
    return render(request,'ecomapp/detail.html',pdata)

def brand_detail(request,id):
    bdata=Product_Detail.objects.get(pk=id)
    bpdata=Brand_Detail.objects.filter(pid=bdata.pk) 
    tdata={'bpdata':bpdata}
    return render(request,'ecomapp/brand.html',tdata)

def final_detail(request,id):
    cdata=Brand_Detail.objects.get(pk=id)
    gdata=Final_Detail.objects.filter(cid=cdata.pk)  
    hdata={'gdata':gdata,'cdata':cdata}
    return render(request,'ecomapp/final.html',hdata)

def conclude_detail(request,cidd,kid):    
    gdata=Final_Detail.objects.filter(cid=cidd)     
    fgdata=Final_Detail.objects.get(pk=kid)
    hdata={'gdata':gdata,'fgdata':fgdata,"cidd":cidd}
    return render(request,'ecomapp/conclude.html',hdata)




