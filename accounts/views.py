# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import RegistrationUserSerializer
from django.contrib.auth.models import User


# Create your views here.
class UserRegistrationService(generics.CreateAPIView):
    serializer_class = RegistrationUserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        response = super(UserRegistrationService, self).post(request, *args, **kwargs)
        if 'password' in response.data:
            response.data.pop('password')
        return response
