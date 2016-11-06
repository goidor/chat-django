from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import (
    ListUsers,
    list_chats,
    messages
)


urlpatterns = [
    #url(r'^(?P<user_id>\d+)/$', ListChats.as_view(), name='detail'),
    url(r'^(?P<user_id>\d+)/$', list_chats, name="list-chats"),
    #url(r'^(?P<user_id>\d+)/new/$', messages, name='messages_new'),
    url(r'^(?P<user_id>\d+)/(?P<room_id>\d+)/$', messages, name='messages'),
    #url(r'^(?P<pk>\d+)/$', ListChats.as_view(), name='detail'),
    #url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    #url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),
    url(r'^', ListUsers.as_view(), name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
