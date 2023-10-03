from .models import back
from django.shortcuts import render

def index(request):
	backs = back.objects.all()
	return render(request, 'back/index.html', {'backs': backs})