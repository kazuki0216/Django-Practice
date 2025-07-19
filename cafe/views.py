from django.http import HttpResponse
from django.shortcuts import render

# List of sample cafe menus
menu_items = [
    "Espresso",
    "Latte",
    "Cappuccino",
    "Americano",
    "Macchiato",
    "Flat White",
    "Mocha",
    "Iced Coffee",
    "Cold Brew",
    "Tea"
]

def cafe_menu(request):
    return HttpResponse("<br>".join(menu_items))  



def order(request):
    return HttpResponse("Hello, world. Claude Sonnet is one of the industry leading llm model.")