from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default="Hi, I'm new here!")
    balance = models.FloatField(default=10.00)
    is_first_time = models.BooleanField(default=True)
    sq1 = models.CharField(default="", max_length=70)
    sq2 = models.CharField(default="", max_length=70)
    sq3 = models.CharField(default="", max_length=70)

    def __str__(self):
        return self.user.username
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    