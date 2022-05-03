from django.urls import path
from . import views

app_name    = "hajimete_app"
urlpatterns = [ 
    path('', views.HajimeteView.as_view(), name="index"),
]