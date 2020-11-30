from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^electrical$', display_electrical, name="display_electrical"),
    url(r'^mechanical$', display_mechanical, name="display_mechanical"),
    url(r'^cleaning$', display_cleaning, name="display_cleaning"),

    url(r'^add_electrical$', add_electrical, name="add_electrical"),
    url(r'^add_mechanical$', add_mechanical, name="add_mechanical"),
    url(r'^add_cleaning$', add_cleaning, name="add_cleaning"),

    url(r'^electrical/edit_item/(?P<pk>\d+)$', edit_electrical, name="edit_electrical"),
    url(r'^mechanical/edit_item/(?P<pk>\d+)$', edit_mechanical, name="edit_mechanical"),
    url(r'^cleaning/edit_item/(?P<pk>\d+)$', edit_cleaning, name="edit_cleaning"),

    url(r'^electrical/delete/(?P<pk>\d+)$', delete_electrical, name="delete_electrical"),
    url(r'^mechanical/delete/(?P<pk>\d+)$', delete_mechanical, name="delete_mechanical"),
    url(r'^cleaning/delete/(?P<pk>\d+)$', delete_cleaning, name="delete_cleaning"),

]
