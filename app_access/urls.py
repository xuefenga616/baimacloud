
from django.conf.urls import url,include
from app_access import views

urlpatterns = [
    url(r'^login/$', views.acc_login, name="acc_login"),
    url(r'^logout/$', views.acc_logout, name="acc_logout"),

]
