from django.shortcuts import render


def index(request):
	return render(request, 'jessicadeaton/index.html', {})

def post_list(request):
	return render(request, 'jessicadeaton/post_list.html', {})

def now(request):
	return render(request, 'jessicadeaton/now.html', {})

def about(request):
	return render(request, 'jessicadeaton/about.html', {})