# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework import filters
from serializers import ToDoItemSerializer
from rest_framework import permissions
from models import ToDoItem


class ToDoItemRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ToDoItem.objects.filter(owner=user)


class ToDoItemCreate(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = ToDoItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('isFinished',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ToDoItem.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

