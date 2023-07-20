from django.shortcuts import render, HttpResponse, redirect

def paises(request):
   return render(request,"paises.html")
def registrarpaises(request):
   return render(request,"registrarpaises.html")
def editoriales(request):
   return render(request,"editoriales.html")
def registrareditoriales(request):
   return render(request,"registrareditoriales.html")
def index(request):
    return render(request,"index.html")