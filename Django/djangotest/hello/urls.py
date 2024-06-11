from django.urls import path

from.import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("krish", views.krish, name="krish"),
    path("beachoo", views.beachoo, name="beachoo")
]