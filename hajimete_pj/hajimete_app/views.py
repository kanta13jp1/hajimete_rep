from django.shortcuts import render
from django.views import View

class HajimeteView(View):
    def get(self, request, *args, **kwargs):

        return render(request,"hajimete_app/index.html")