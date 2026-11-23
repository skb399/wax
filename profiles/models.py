from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    """
    Stores a registered customer's default delivery information.
    """
    # user associated with this profile, has a one-to-one relationship with the
    # profile, each user has one profile
    user = models.OneToOneField(
        # References Django's configured user model
        settings.AUTH_USER_MODEL,
        # If the user is deleted, the profile will also be deleted
        on_delete=models.CASCADE,
        # this allows access to user profile from the user instance via
        # 'userprofile' attribute of the user model
        related_name='userprofile'
    )
    # fields for storing the user's default delivery information, blank=true
    # allows them to be optional so a user can have a profile without filling
    # in all the details. We do not need the email field as this data is
    # already stored in the user model.
    default_phone_number = models.CharField(max_length=20, blank=True)
    default_address_line1 = models.CharField(max_length=80, blank=True)
    default_address_line2 = models.CharField(max_length=80, blank=True)
    default_town_or_city = models.CharField(max_length=40, blank=True)
    default_county = models.CharField(max_length=80, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_country = CountryField(blank=True)

    # This makes our model instances easier to read in Django Admin by
    # displaying the associated user's username.
    def __str__(self):
        return self.user.username
