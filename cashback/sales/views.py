from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Costumer, Product, CashBack

# Create your views here.
@api_view(['GET', 'POST'])
def costumer(request):
    pass





