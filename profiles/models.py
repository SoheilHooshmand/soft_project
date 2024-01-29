from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, null = True, blank = True)
    email = models.EmailField(max_length = 500, null = True, blank = True)
    username = models.CharField(max_length = 200, null = True, blank = True)
    short_intro = models.CharField(max_length = 200, null = True, blank = True)
    bio = models.TextField(null = True, blank = True)
    profile_image = models.ImageField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return str(self.name)


class Lawyer(models.Model):
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE, primary_key = True)
    experience = models.IntegerField(default = 0, null = True, blank = True)




class Expertise(models.Model):
    name = models.CharField(max_length = 100, null = True, blank = True)
    owner = models.ForeignKey(Lawyer, on_delete = models.CASCADE, null = True, blank = True, related_name='expertises')
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return str(self.name)

class Client(models.Model):
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE, primary_key = True)
    lawyers = models.ManyToManyField(Lawyer, null = True, blank = True, related_name = 'clients')



class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True)
    recipient = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'messages')
    name = models.CharField(max_length = 100, null = True, blank = True)
    subject = models.CharField(max_length = 200, null = True, blank = True)
    body = models.TextField()
    is_read = models.BooleanField(default = False, null = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']



