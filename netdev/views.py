#Django native imports
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _

# Import from our apps
from netdev.models import Netdev


class NetdevList(generic.ListView):
    """
    List view for the network devices
    """
    model = Netdev
    template_name = 'netdev/netdev_list.html'
    paginate_by = 50

class NetdevDetail(generic.DetailView):
    """
    Detail view for a single network device. This view is shown on the webpage
    when user clicks on a single network device on "Netdev list" page
    """

    model = Netdev
    template_name = 'netdev/netdev_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(NetdevDetail, self).get(request, *args, **kwargs)