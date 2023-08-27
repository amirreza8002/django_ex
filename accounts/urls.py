from django.urls import include, path

from . import views

urlpatterns = [
    path("", include("allauth.urls")),
    path("loggedout/", views.LoggedOut.as_view(), name="logged_out"),
]
