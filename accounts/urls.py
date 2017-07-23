from django.conf.urls import include, url
from .views import UserRegistrationService


urlpatterns = [
    url(r'^register/', UserRegistrationService.as_view()),
]
