import os
import stripe

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
from dotenv import load_dotenv

from .models import Item

load_dotenv()

stripe.api_key=os.getenv('API_KEY')

def buy(request, pk):
    item = Item.objects.get(id=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': item.name,
                'description': item.description
                },
            'unit_amount': item.price,
            },
            'quantity': 1,
        }],
    mode='payment',
    success_url='http://localhost:8000/success',
    cancel_url='http://localhost:8000/cancel',
    )
    return redirect(session.url, code=303)

def item(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'pk': pk,
        'name': item.name,
        'description': item.description,
        'price': item.price,
    }
    return render(request, 'item.html',context)

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'    
