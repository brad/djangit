from django.db import models

class Server(models.Model):
    user = models.CharField(max_length=50)
    domain = models.CharField(max_length=200)
    def __unicode__(self):
        return self.domain

class Repo(models.Model):
    project_name = models.CharField(max_length=50)
    repo = models.CharField(max_length=200)
    def __unicode__(self):
        return self.project_name
    
class Branch(models.Model):
    TYPE_CHOICES = ( 
        ('B', 'Beta'),
        ('R', 'Release'),
    ) 
    server = models.ForeignKey(Server)
    repo = models.ForeignKey(Repo)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    source = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    url = models.URLField()
    def __unicode__(self):
	if self.type == 'B':
            return 'Beta - ' + str(self.repo)
        else:
            return 'Release - ' + str(self.repo)

class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(Branch)
    commit = models.CharField(max_length=200)
    def __unicode__(self):
        return self.created + ' - ' + self.branch + ' - ' + self.commit
    
