from django.conf.urls import url
from .views import profile_detail,create_profile,edit_profile
urlpatterns = [
    url(r'^create/', create_profile, name="createprofile" ),
    url(r'^detail/', profile_detail, name="profiledetails" ),
    url(r'^edit/',edit_profile,name = "edit"),
]
