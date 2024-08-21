from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from usuarios.models import Users

# Create your views here.


@login_required
def ciurb(request):
    if request.method == "GET":
        return render(request, 'ciurb.html')


@login_required
def multimissao(request):
    if request.method == "GET":
        return render(request, 'multimissao.html')


@login_required
def salvamento(request):
    if request.method == "GET":
        return render(request, 'salvamento.html')


@login_required
def motorresgate(request):
    if request.method == "GET":
        return render(request, 'motorresgate.html')
