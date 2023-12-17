from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Tovar


def index(request):
	data = Tovar.objects.all()
	return render(request, "index.html", {"data": data})

def update(request):
	if request.method == 'POST':
		tov = Tovar()
		tov.name = request.POST.get('name')
		tov.infotov = request.POST.get('info')
		tov.price = request.POST.get('price')
		tov.save()
	return HttpResponseRedirect("../")

def red(request):
	return HttpResponse("Если надо отредактировать или удалить, то заходите в <a href='../../admin/'>admin</a> панель и там всё делайте, мне лень это реальзовывать)")