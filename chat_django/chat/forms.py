# -*- coding: utf-8 -*-
from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.models import User

from .models import Message


class MessageSendForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('user', 'room', 'time')
