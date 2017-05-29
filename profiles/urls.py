from django.conf.urls import url

from .views import sign_in, sign_up, sign_out
from . import views

# app_name = 'profiles'
urlpatterns = [
    url(r'^registration/sign-in/$', sign_in, name='sign_in'),
    url(r'^registration/sign-up/$', sign_up, name='sign_up'),
    url(r'^sign-out/$', sign_out, name='sign_out'),
    url(r'^item/add/$', views.ItemCreate.as_view( success_url= '/'), name = 'item-add'),
]