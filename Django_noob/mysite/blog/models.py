from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    # Allows us to reference Post.title and get a string
    # instead of <class object Post @ 0x0302023> junk
    def __str__(self):
        return self.title
