from django.contrib import admin

from chat.models import Room, Message


class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)


class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
