from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    last_message = models.ForeignKey('Message', blank=True, null=True, verbose_name='Last message', related_name='last_messages')

    def __str__(self):
        return self.user.username

class Message(models.Model):
    user = models.ForeignKey(User)
    room = models.ForeignKey(Room, related_name='messages')
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return '[%s]: %s' % (self.time, self.message)

    def room_post_save(sender, instance, created, **kwargs):
        Room.objects.get_or_create(user=instance.user_id)

    def message_post_save(sender, instance, created, **kwargs):
        Room.objects.filter(id=instance.user_id).update(last_message=instance)
