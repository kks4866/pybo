from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


# 답변 모델(테이블
class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #외래키 제약조건 무시하고 연쇄 삭제 됨
    content = models.TextField()
    create_date = models.DateTimeField()

