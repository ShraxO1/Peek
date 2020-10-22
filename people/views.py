from django.shortcuts import render
from .models import People
# Create your views here.

def people_list(request):
	obj = People.objects.all()
	return render(request, 'people/people.html', {'obj':obj})
