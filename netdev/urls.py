#Django native imports
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from django.views.generic import edit
#from django.views.generic.base import TemplateView

# Import from our apps
from netdev import views


urlpatterns = [
    #url(r'^service1', TemplateView.as_view(template_name='service1.html'), name='service1'),
    url(r'^routerlist$', views.RouterList.as_view(), name='router_list'),
    url(r'^firewalllist$', views.FirewallList.as_view(), name='firewall_list'),
    url(r'^switchlist$', views.SwitchList.as_view(), name='switch_list'),
    url(r'^otherlist$', views.OtherList.as_view(), name='other_list'),
    url(r'^(?P<pk>\d+)/$', views.NetdevDetail.as_view(), name='netdev_detail'),
    ]
