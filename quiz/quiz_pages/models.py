from django.db import models

# Create your models here.
class Theme(models.Model):
    theme_text = models.CharField(max_length=200)

    def __str__(self):
        return self.theme_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_valid_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text