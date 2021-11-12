from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

class newtaskform(forms.Form):
    tasks = forms.CharField (label="name")
    priority = forms.IntegerField (label="number",min_value=2,max_value=16)

#create your own views here

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request,"task/index.html" , {
        "tasks" : request.session["tasks"]
    })

def add(request):
    print(request.method)
    
    if request.method == "post":
        form = newtaskform(request.post)
        print(form.is_valid())
        if form.is_valid():
            task = form.cleaned_data("task")
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse,"task/index.html")

        else:
            return render(request ,"task/add.html", {
                "form": forms
            })

    return render(request , "task/add.html",{
        "forms" : newtaskform()
    })

def layout(request):
    return render(request, "task/layout.html")    