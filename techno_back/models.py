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