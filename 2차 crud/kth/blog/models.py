from django.db import models

# Create your models here.

class Article(models.Model): # 모델안에 있는 것들을 사용하기 위해 상속을 함
    title = models.CharField(max_length=20)
    content = models.TextField()  # textfield는 글 쓰는 제한이 더 적다.
    created_at = models.DateTimeField(auto_now_add=True) # 시간을 받는 함수. // 자동으로 지금 생성한 시간이 저장이 됨.
    published_at = models.DateTimeField(null=False)  # 빈값을 허용하지 않겠다.

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")  # 외래키라..
    content = models.CharField(max_length=100) # 최대 

    def __str__(self):
        return self.content
