from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, default='🏆')
    color = models.CharField(max_length=20, default='#3b82f6')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('closed', 'Closed'), ('upcoming', 'Upcoming')]
    TYPE_CHOICES = [('online', 'Online'), ('offline', 'Offline'), ('hybrid', 'Hybrid')]

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    organizer = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    event_date = models.DateTimeField()
    deadline = models.DateTimeField()
    location = models.CharField(max_length=300)
    link_online = models.URLField(blank=True)
    event_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='online')
    price = models.CharField(max_length=100, default='Gratis')
    benefit = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def is_deadline_near(self):
        return self.deadline - timezone.now() <= timezone.timedelta(days=3)

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=200)
    npm = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    batch_year = models.CharField(max_length=4)
    motivation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
