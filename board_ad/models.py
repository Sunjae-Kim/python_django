from django.db import models


# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='Happy Hacking')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title[:20]}'


class Comment(models.Model):
    # `models.CASCADE` Posting 이 삭제되면 댓글도 다 삭제되도록 설정함
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.content[:30]}'
