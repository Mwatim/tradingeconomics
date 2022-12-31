from django.shortcuts import render, HttpResponse
from demoapp.scripts import get_mexico_demo, get_kenya_uganda_trade


# Create your views here.
def base(request):
    """
    Returns a Table with Mexico GDP Variables, Kenya Imports from Uganda.
    """
    return HttpResponse([get_mexico_demo().T.to_html(classes='table table-stripped'), get_kenya_uganda_trade().T.to_html(classes='table table-stripped')])

def index(request):
    """
    Returns Sample Trade Data on Kenya Imports from Uganda
    """
    # mexico_response = HttpResponse(get_mexico_demo().T.to_html(classes='table table-stripped'))
    # kenya_uganda_response = HttpResponse(get_kenya_uganda_trade().T.to_html(classes='table table-stripped'))
    return HttpResponse([get_mexico_demo().T.to_html(classes='table table-stripped'), get_kenya_uganda_trade().T.to_html(classes='table table-stripped')])