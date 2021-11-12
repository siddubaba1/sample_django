from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),   
    path("gelos", views.gelos, name="gelos"),
    path("rufus", views.rufus ,name="rufus"),
    path("<str:name>",views.greet, name="greet")
]