from django.shortcuts import render,get_object_or_404
from .models import *
from evento.models import *
import datetime

# Create your views here.

def index_galeriasImagenes(request, template = 'list_galeria.html'):
	list_galeria = GaleriaImagenes.objects.order_by('-id')

	return render(request,template,locals())

def detalle_galeriaImagenes(request, slug, template = 'detail_galeria.html'):
	object = GaleriaImagenes.objects.get(slug = slug)
	related_gal = GaleriaImagenes.objects.filter(tematica = object.tematica)
	latest_gal = GaleriaImagenes.objects.order_by('-id')[:9]
	return render(request, template, locals())

def filtro_temas_img(request,tema,template="list_galeria.html"):
	return render(request,template,locals())


def index_galeriaVideos(request,template = 'list_galeria.html'):
	list_galeria = GaleriaVideos.objects.order_by('-id')

	return render(request,template,locals())

def detalle_galeria_vid(request,slug,template ='detail_galeria_vid.html'):
	object = GaleriaVideos.objects.get(slug = slug)
	return render(request,template,locals())

def filtro_temas_vid(request,tema,template='list_galeria.html'):
	list_galeria = GaleriaVideos.objects.filter(tematica = tema).order_by('-id')

	return render(request,template,locals())
