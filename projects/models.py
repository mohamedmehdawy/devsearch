from django.db import models
from users.models import Profile
import uuid

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=2000)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default="default.jpg")
    tags = models.ManyToManyField('Tag', blank=True)
    demo_link = models.URLField(max_length=2000, null=True, blank=True)
    source_link = models.URLField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def reviewers(self):
        return self.review_set.all().values_list('owner', flat=True)
    
    def calcVote(self):
        reviews = self.review_set.all()
        up_reviews = reviews.filter(value="up").count()
        self.vote_total = reviews.count()
        try:
            self.vote_ratio = (up_reviews / self.vote_total) * 100
        except:
            self.vote_ratio = 0
        self.save()

    def __str__(self):
        return self.title
    

        
    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "title"]


class Review(models.Model):
    VOTE_TYPE = [
        (
            'up',
            'Up Vote'
        ),
        (
            'down',
            'Down Vote'
        ),
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length= 200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = ['owner', 'project']


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
