from tkinter import CASCADE
from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default="")
    def __str__(self):
        return (self.userName)
    class Meta:
        db_table = "user"

class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100)
    projectDescription = models.CharField(max_length=300)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (self.projectName)
    class Meta:
        db_table = "project"

class Issue(models.Model):
    issueId = models.AutoField(primary_key=True)
    issueName = models.CharField(max_length=100)
    issueType = models.CharField(max_length=100)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigneeId = models.ForeignKey(User, on_delete=models.CASCADE)
    reporterId = models.IntegerField()
    issueStatus = models.IntegerField()
    issueDescription = models.CharField(max_length=300)
    def __str__(self):
        return (self.issueName)
    class Meta:
        db_table = "issue"

class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30,null=True)
    authorId = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    issueId = models.ForeignKey(Issue, on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=200,null=True)
    createdOn = models.DateTimeField(null=True)
    updatedOn = models.DateTimeField(null=True)
    def __str__(self):
        return 'comment by %s on %s' % (self.author, self.issueId)
    class Meta:
        db_table = "comment"
