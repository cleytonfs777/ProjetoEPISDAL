from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def criaplano(request):
    return render(request, 'criaplano.html')
