from django import forms
from .models import Books, IssueBooks
from django.forms import ModelForm
from django.contrib.auth.models import User


class addBooksForm(forms.ModelForm):
    isbn = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
        required=True, max_length=40)
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Book Name'}),
        required=True, max_length=50)
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Author'}),
        required=True, max_length=50)
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        required=True)

    class Meta:
        model = Books
        fields = [
            'isbn',
            'title',
            'author',
            'quantity'
        ]
        ordering = ['title']


class IssueBooksForm(forms.ModelForm):
    class Meta:
        model = IssueBooks
        fields = [
            'issue_book',
            'issue_by',
        ]
        ordering = ['issue_book']
