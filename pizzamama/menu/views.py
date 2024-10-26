from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
def index(request):
    pizzas =Pizza.objects.all().order_by('prix')
    # pizza_names =[pizza.nom for pizza in pizzas]
    # pizza_prices =[pizza.prix for pizza in pizzas]
    # menu = zip(pizza_names,pizza_prices)
    
    # list_menu = ", ".join([f"{nom} : {prix} £ " for nom, prix in menu ])
    # return HttpResponse(f"Les pizzas : {list_menu}")
    return render(request,"menu/index.html", {'pizzas': pizzas})





