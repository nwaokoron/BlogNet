from django.db import models
from django.contrib.auth.models import User as auth_user
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
# sometime in the future would like to add premuim attribute
#    password = models.CharField(max_length = 200)
#   last_login = models.DateTimeField('Last Login Date', auto_now = True )
#   first_name = models.CharField(max_length = 200)
#   last_name = models.CharField(max_length = 200)
#   email = models.EmailField(unique = True)
#   date_joined = models.DateTimeField('Onboard date')
    user = models.OneToOneField(auth_user, on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    date_of_birth = models.DateField("DoB", null = True)
    bio = models.TextField()
    ranking = models.IntegerField(default = 0)


@receiver(post_save, sender=auth_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=auth_user)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Post(models.Model):
    date_created = models.DateTimeField('when published')
    last_modified = models.DateTimeField('last changed', auto_now = True )
    post_title = models.CharField(max_length = 200)
    post_content = models.TextField()
    post_points = models.IntegerField( default = 0 )
    author = models.ForeignKey(UserProfile, on_delete = models.CASCADE)

class Comment(models.Model):
    date_created = models.DateTimeField('when said')
    last_modified = models.DateTimeField('last edited', auto_now = True)
    comment_content = models.TextField()
    comment_Points = models.IntegerField( default = 0)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    commenter = models.ForeignKey(UserProfile, on_delete = models.CASCADE)


