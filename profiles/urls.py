from django.conf.urls import url

from .views import sign_in, sign_up, sign_out,add_item

urlpatterns = [
    url(r'^sign-in/$', sign_in, name='sign_in'),
    url(r'^sign-up/$', sign_up, name='sign_up'),
    url(r'^sign-out/$', sign_out, name='sign_out'),
    url(r'^add_item/$', add_item, name= 'add_item'),
]