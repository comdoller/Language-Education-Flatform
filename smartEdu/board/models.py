from django.db import models
from datetime import datetime

# Create your models here.

class Board(models.Model):
    idx = models.AutoField(primary_key=True)
    writer = models.CharField(null=False, max_length=50)
    title = models.CharField(null=False, max_length=120)
    hit = models.IntegerField(default=0)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    filename = models.CharField(null=True, default="", max_length=500)
    filesize = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)

    def hit_up(self):
        self.hit += 1

    def down_up(self):
        self.down += 1


class Comment(models.Model):
    idx = models.AutoField(primary_key=True)
    board_idx = models.IntegerField(null=False)  # , foreign_key = board.idx
    writer = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
