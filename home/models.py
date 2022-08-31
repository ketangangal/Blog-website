from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)

    content = RichTextField(blank=True, null=True)

    def display_my_safefield(self):
        if '<script>' in self.content:
            self.is_malicious = True
            self.save()
            return self.content
        return mark_safe(self.content)

    image = models.ImageField(upload_to="profile_pics", blank=False, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blogs')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " Comment: " + self.content


class article(models.Model):
    content = HTMLField()


class textEditor(models.Model):
    title = models.CharField(max_length=20)
    content = HTMLField()

    def __str__(self):
        return str(self.title)
