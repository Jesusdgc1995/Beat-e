from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    # isAdmin = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    profilePhoto = models.ImageField(blank=True, null=True)
    aboutMe = models.TextField(blank=True, null=True)
    numFollowers = models.IntegerField(default=0)
    numFollowing = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.user.email

    def countFollower(self):
        self.numFollowers += 1
        self.save()

    def uncountFollower(self):
        self.numFollowers -= 1
        self.save()

    def countFollowing(self):
        self.numFollowing += 1
        self.save()

    def uncountFollowing(self):
        self.numFollowing -= 1
        self.save()


class ArtistProfile(Profile):
    artisticName = models.CharField(max_length=100)


class UserProfile(Profile):
    def __str__(self) -> str:
        return self.name