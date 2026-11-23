from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import UserProfile

User = get_user_model()

# This receiver function listens for the User model's post-save signal,
# sender=settings.AUTH_USER_MODEL tells Django to listen for changes to the
# User model.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically creates a UserProfile when a new User is created.
    """
    # created is true when a new User instance has been created.
    if created:
                # get_or_create() creates a profile if one doesn't already
                # exist.
                # instance represents the actual User object that triggered the
                # post_save signal. This instance is used to create the
                # associated UserProfile.
        UserProfile.objects.get_or_create(user=instance)