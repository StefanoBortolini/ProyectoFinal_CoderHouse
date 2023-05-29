from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppTienda/index.html',
        context=contexto,
    )
    return http_response


def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppTienda/about.html',
        context=contexto,
    )
    return http_response