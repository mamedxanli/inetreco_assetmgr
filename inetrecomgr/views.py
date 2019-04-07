#Django native imports
from django.views import generic
from django.shortcuts import render, render_to_response

# Python imports
from itertools import chain

# Import from our apps
from netdev.models import Netdev
from server.models import Server


class HomePage(generic.TemplateView):
    template_name = "inetrecomgr/index.html"
    context_object_name = 'context'