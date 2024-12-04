from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Model representing the About page content.

    Attributes:
        title (str): Title of the about page section.
        profile_pic (CloudinaryField): Profile picture for the about page.
        updated_on (datetime): Timestamp of the last update.
        content (str): Content of the about page section.
    """
    title = models.CharField(max_length=200)
    profile_pic = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class RequestNewQuest(models.Model):

    """
    Model representing a request for a new quest.

    Attributes:
        fname (str): First name of the requester.
        lname (str): Last name of the requester.
        email (str): Email address of the requester.
        message (str): Message from the requester.
        image (CloudinaryField): Image provided by the requester.
        read (bool): Status indicating if the request has been read.
    """

    fname = models.CharField('First Name', max_length=200)
    lname = models.CharField('Last Name', max_length=200)
    email = models.EmailField()
    message = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    read = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"New quest request from {self.fname} {self.lname}"
        )
