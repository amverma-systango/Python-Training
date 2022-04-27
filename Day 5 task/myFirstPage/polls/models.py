from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField( max_length = 50 )
    user_password = models.CharField( max_length = 20 )

    def __str__(self):
        return str(self.id)





class Question(models.Model):
    owner_id = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.id)





class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    choice_text = models.CharField( max_length=200 ) 
    votes = models.IntegerField( default = 0 )

    def __str__(self):
        return str(self.id)





class Participant(models.Model):

    participant_id = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    choice_id = models.ForeignKey(Choice, on_delete = models.CASCADE, default=None)

    def __str__(self):
        return str(self.id)