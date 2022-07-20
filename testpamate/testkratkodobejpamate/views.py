from django.shortcuts import render
from django.http import HttpResponse
import random




def home(request):
	context = {
	}
	return render(request, 'testkratkodobejpamate/home.html', context)

def about(request):
	return render(request, 'testkratkodobejpamate/about.html')

def testkid(request):
	return render(request, 'testkratkodobejpamate/testkid.html' )

def teststudent(request):
	context = {
		'cislo': str(random.randint(10000, 99999)),
	}
	return render(request, 'testkratkodobejpamate/teststudent.html', context)

def testadult(request):
	context = {
		'cislo1': str(random.randint(0, 9)),
		'cislo2': str(random.randint(0, 9)),
		'cislo3': str(random.randint(0, 9)),
		'cislo4': str(random.randint(0, 9)),
		'cislo5': str(random.randint(0, 9)),
	}
	return render(request, 'testkratkodobejpamate/testadult.html', context)

def testsenior(request):
	context = {
		'cislo': str(random.randint(10000, 99999)),
	}
	return render(request, 'testkratkodobejpamate/testsenior.html', context)

def results(request):
	return render(request, 'testkratkodobejpamate/results.html')

# Create your views here.

def wait(request):
    time.sleep(3)
    return HttpResponse("Done")