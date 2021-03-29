from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	j = 1
	context = {'j': j}
	return render(request, 'ajax/home.html', context)
# Create your views here.
def counting(request):
	j = 1

	context = {'j': j}

	if request.method == "GET":

		j = request.GET['count']
		count = context['j']
		count+=int(j)

		

		return HttpResponse(f'{count}')
	

	
	