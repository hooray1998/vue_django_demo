from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
import requests
import json

from .models import Book

@require_http_methods(["POST"])
def textparse_check(request):
    response = {}
    form_data = json.loads(request.body.decode())
    print('template:', form_data['template'])
    try:
        response['result'] = """
fasd
fafasdf
        """
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["POST"])
def textparse_parse(request):
    response = {}
    form_data = json.loads(request.body.decode())
    print('template:', form_data['template'])
    try:
        response['result'] = """
fasd
fafasdf
        """
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        #  book = Book(book_name=request.GET.get('book_name'))
        #  book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = ['afds', 'fasdf']
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
