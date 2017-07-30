from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = "scamBlastRApp"
urlpatterns = [ url(r'^home/$', views.home, name='home'),
                url(r'^login/$', views.login, name='login'),
              ]
