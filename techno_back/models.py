from django.db import models
from django.urls import reverse


class Feedback(models.Model):
    """
    Model representing user's feedback.
    """
    user_email = models.EmailField(max_length=200, help_text="example@example.com")
    feedback = models.TextField(max_length=1000, help_text="Напишіть свій відгук тут...")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s\n\"%s\"' % (self.user_email, self.feedback)

    def get_absolute_url(self):
        """
        Returns the url to access a particular feedback instance.
        """
        return reverse('feedback-detail', args=[str(self.id)])


class Artist(models.Model):
    nickname = models.CharField(max_length=30, help_text="Нікнейм артиста")
    index_img = models.CharField(max_length=200, help_text="URL картинки на головній сторінці")
    index_info = models.TextField(max_length=1000, help_text="Коротке інфо артиста")
    full_info = models.TextField(max_length=2000, help_text="Повне інфо артиста")
    carousel1 = models.ImageField(upload_to="carousel-images/", help_text="1 картинка артиста")
    carousel2 = models.ImageField(upload_to="carousel-images/", help_text="2 картинка артиста", blank=True, null=True)
    carousel3 = models.ImageField(upload_to="carousel-images/", help_text="3 картинка артиста", blank=True, null=True)
    bandcamp = models.URLField(max_length=200, help_text="Bandcamp-link")
    instagram = models.URLField(max_length=200, help_text="Instagram-link")
    soundcloud = models.URLField(max_length=200, help_text="Soundcloud-link")
    soundcloud_api = models.TextField(max_length=1200, help_text="Soundcloud Plugin", default="default")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nickname

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('artist', args=[str(self.id)])
