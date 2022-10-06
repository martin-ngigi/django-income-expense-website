from django.shortcuts import render

# Create your views here.

def index(request):
    #render template from templates/expenses/index.html
    return render(request, 'expenses/index.html')

def add_expense(request):
    return render(request, 'expenses/add_expense.html')
