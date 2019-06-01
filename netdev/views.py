#Django native imports
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _

# Import from our apps
from netdev.models import Netdev

class RouterList(generic.ListView):
    """
    List view for the router devices
    """
    model = Netdev
    template_name = 'netdev/router_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Netdev.objects.filter(device_type="router")
        return qs.order_by("pk")

class FirewallList(generic.ListView):
    """
    List view for the firewall devices
    """
    model = Netdev
    template_name = 'netdev/firewall_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Netdev.objects.filter(device_type="firewall")
        return qs.order_by("pk")

class SwitchList(generic.ListView):
    """
    List view for the switch devices
    """
    model = Netdev
    template_name = 'netdev/switch_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Netdev.objects.filter(device_type="switch")
        return qs.order_by("pk")

class OtherList(generic.ListView):
    """
    List view for the router devices
    """
    model = Netdev
    template_name = 'netdev/other_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Netdev.objects.filter(device_type="other")
        return qs.order_by("pk")

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