from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm



# Create your views here.

def home(request):
    submitted = False

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = StudentForm()

    return render(request, 'forms/home.html', {'form': form, 'submitted': submitted})

    



