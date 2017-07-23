from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^todo/(?P<pk>[-\w]+)/$', views.ToDoItemRetrieveUpdate.as_view()),
    url(r'^todo/$', views.ToDoItemCreate.as_view())
]
