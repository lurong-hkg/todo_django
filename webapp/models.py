# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ToDoItem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    content = models.CharField(unique=False, max_length=240, blank=False, default='')
    isFinished = models.BooleanField(blank=False, default=False)
    created = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        ordering = ('created',)
