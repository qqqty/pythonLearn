from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username

#time
class Vote(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    auth = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __unicode__(self):
        return self.title

class VoteItem(models.Model):
    vote_id = models.IntegerField()
    item = models.CharField(max_length=20)

    def __unicode__(self):
        return self.item

class VoteAccount(models.Model):
    vote_id = models.IntegerField()
    item_id = models.IntegerField()
    acc_id = models.IntegerField()

    def __unicode__(self):
        return self.acc_id
