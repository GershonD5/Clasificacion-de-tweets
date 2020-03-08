from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)
    ofensivo= models.IntegerField(default=0)
    total= models.IntegerField(default=0)
    def __str__(self):
        return self.tweet_text

#class Choice(models.Model):
 #   tweet= models.ForeignKey(Tweet, on_delete=models.CASCADE)
 #   choice_text= models.CharField(max_length=200)
 #   votes = models.IntegerField(default=0)
#
#    def __str__(self):
#        return self.choice_text
