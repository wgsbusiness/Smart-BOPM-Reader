from django.shortcuts import render

# relative import of forms
from .models import User


from django.views.generic import TemplateView


class HomePageUsersView(TemplateView):
    template_name = "users.html"




def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context = {}

	# add the dictionary during initialization
	context["dataset"] = User.objects.all()

	return render(request, "users.html", context)
