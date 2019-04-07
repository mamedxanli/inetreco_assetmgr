#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from server.models import Server


class ServerList(generic.ListView):
    """
    List view for the servers
    """
    model = Server
    template_name = 'server/server_list.html'
    paginate_by = 50


class ServerDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = Server
    template_name = 'server/server_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ServerDetail, self).get(request, *args, **kwargs)