from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date

# Create your models here.


class Books(models.Model):
    isbn = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']


class IssueBooks(models.Model):

    def get_entry_date():
        return datetime.today()

    def get_expiry_date():
        return datetime.today()+timedelta(days=8)

    def get_fine(self):
        fine = (date.today()-self.expiry_date).days
        if fine > 0:
            fine = fine
        else:
            fine = 0
        return fine

    issue_book = models.ForeignKey(Books, on_delete=models.CASCADE)
    issue_by = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField(default=get_entry_date)
    expiry_date = models.DateField(default=get_expiry_date)

    def __str__(self):
        return f'{self.issue_book}-{self.issue_by} [{self.entry_date} to {self.expiry_date}]'
