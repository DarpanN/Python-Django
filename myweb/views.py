from django.http import HttpResponse
from django.shortcuts import render


#here we need to call 2 function parament (Request//index.html)
#data passing  throught view
def homePage(request):
  
    return render(request, "index.html")

def fashionPage(request):
  
    return render(request, "fashion.html")

def jewelleryPage(request):
  
    return render(request, "jewellery.html")

def electronicPage(request):
  
    return render(request, "electronic.html")

    






