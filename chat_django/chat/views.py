from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import (
    CreateView,
    UpdateView
)
from django.contrib.auth.models import User

from .models import Room, Message
from .forms import MessageSendForm


class ListUsers(ListView):
    model = User
    context_object_name = 'user_list'
    queryset = User.objects.filter(is_active=True, is_superuser=False)
    template_name = 'chat/user_list.html'


def list_chats(request, user_id):
    if user_id is not None:
        user = User.objects.get(id=user_id)
        users = User.objects.filter(~Q(id=user_id), is_active=True, is_superuser=False)

        return render(request, 'chat/room_list.html',
            {'list_users': users,
            'usuario': user.id})
    else:
        return render(request, 'chat/room_list.html')


def messages(request, user_id, room_id=None):
    user = User.objects.get(id=user_id)
    form = MessageSendForm()
    if request.method == 'POST':
        form = MessageSendForm(request.POST)
        if form.is_valid():
            #import pdb; pdb.set_trace()
            room_chat = Room.objects.get(id=room_id)
            message = form.save(commit=False)
            message.message = request.POST['message']
            message.room = room_chat
            message.user = user
            message.save()

    if room_id:
        room_chat, created = Room.objects.get_or_create(user=user_id)
        #messages = Message.objects.filter(room=room_chat[0], user=)
        messages = reversed(room_chat.messages.order_by('-time')[:50])
        users = User.objects.filter(~Q(id=user_id), is_active=True, is_superuser=False)

        return render(request, 'chat/chat.html',
            {'messages': messages,
            'users': users,
            'user_chat': user.username,
            'usuario': user.id,
            'user_name': '%s %s' % (user.first_name, user.last_name),
            'form': form})
    else:
        return render(request, 'chat/room_list.html')
