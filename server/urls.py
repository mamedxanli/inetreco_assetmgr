#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from server import views

urlpatterns = [
    url(r'^list$', views.ServerList.as_view(), name='server_list'),
    url(r'^(?P<pk>\d+)/$', views.ServerDetail.as_view(), name='server_detail'),
              ]