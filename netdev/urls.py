#Django native imports
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from django.views.generic import edit

# Import from our apps
from netdev import views


urlpatterns = [
    url(r'^list$', views.NetdevList.as_view(), name='netdev_list'),
    url(r'^(?P<pk>\d+)/$', views.NetdevDetail.as_view(), name='netdev_detail'),
    ]
