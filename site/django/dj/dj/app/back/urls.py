from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from back.views import index


urlpatterns = [
	path('', index, name = 'index')
]
