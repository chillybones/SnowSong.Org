from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django import template


def index(request):
    page_title = 'SnowSong Labs'

    context = {
        'page_title': page_title,
    }

    return render(request, 'index.html', context)