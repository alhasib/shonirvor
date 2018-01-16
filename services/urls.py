from django.conf.urls import url
from .views import service_catagory, service_add, service_details, catagorywise_service

urlpatterns = [
    url(r'^service_catagory/', service_catagory, name='service_catagory'),
    url(r'^service_add/', service_add, name='service_add'),
    url(r'^service_details/(?P<provider>\w+)/', service_details, name='service_details'),
    url(r'^catagorywise_service/(?P<service_catagory>\w+)/$', catagorywise_service, name='catagorywise_service'),
]
