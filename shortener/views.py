from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *

def home_view(request):
    context = {}
    context['form'] = shortener_form()
    
    if request.method == "GET":
        return render(request,"home.html",context)
    
    elif request.method == "POST":
        used_form = shortener_form(request.POST)

        if used_form.is_valid():
            shortened_object=used_form.save()

            new_url = request.build_absolute_uri('/')+shortened_object.short_url

            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, 'home.html', context)
        

        context['errors'] = used_form.errors

        return render(request, 'home.html', context)
    
def redirect_url_view(request,shortened_part):
    try:
        shortener = Shortener.objects.get(short_url = shortened_part)
        shortener.times_followed += 1
        shortener.save()

        return HttpResponseRedirect(shortener.long_url)
    
    except:
        raise Http404("Sorry this link is broken:(")
