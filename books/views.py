from django.shortcuts import render, redirect
from .models import Books, IssueBooks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from .forms import addBooksForm, IssueBooksForm
from django.contrib.auth.models import User
from .filters import IssueFilter
# Create your views here.


def search(request):
    books = Books.objects.all()
    if request.method == 'POST':
        search = request.POST["book"]
        if search:
            match = Books.objects.filter(Q(title__icontains=search))
            if match:
                context = {
                    'books': match
                }
                return render(request, 'books/searchresults.html', context)
            else:
                context = {
                    'books': books,
                    'message': 'No results Found'
                }
                return render(request, 'books/searchresults.html', context)

        context = {
            'books': books,
            'message': 'Please enter book name'
        }
        return render(request, 'books/searchresults.html', context)

    else:
        context = {
            'books': books
        }
        return render(request, 'books/searchbooks.html', context)


def add_books(request):
    books_form = addBooksForm()
    if request.method == 'POST':
        books_form = addBooksForm(request.POST)
        if books_form.is_valid():
            books_form.save()
            return HttpResponseRedirect(reverse("index"))
    context = {
        'books_form': books_form
    }
    return render(request, 'books/addbooks.html', context)


def issue_books(request):
    issuebooks_form = IssueBooksForm()
    if request.method == 'POST':
        issuebooks_form = IssueBooksForm(request.POST)
        if issuebooks_form.is_valid():
            book = issuebooks_form.cleaned_data['issue_book']
            database_book = Books.objects.get(title=book)
            if database_book.quantity <= 0:
                context = {
                    'message': 'Book not available'
                }
                return render(request, 'library/error.html', context)
            database_book.quantity -= 1
            database_book.save()
            issuebooks_form.save()
            return HttpResponseRedirect(reverse("viewissuebooks"))
    context = {
        'issuebooks_form': issuebooks_form,
    }
    return render(request, 'books/issuebooks.html', context)


def issue_books_view(request):
    issue_list = IssueBooks.objects.all()
    myFilter = IssueFilter(request.GET, queryset=issue_list)
    issue_list = myFilter.qs
    context = {
        'issue_list': issue_list,
        'myFilter': myFilter
    }
    return render(request, 'books/viewissuebooks.html', context)


def return_book(request, id):
    try:
        book = IssueBooks.objects.get(id=id)
        return_book = book.issue_book
        database_book = Books.objects.get(title=return_book)
        database_book.quantity += 1
        database_book.save()
        book.delete()
    except book.DoesNotExist:
        return
    return HttpResponseRedirect(reverse('viewissuebooks'))


def student_issuedbooks(request):
    books = IssueBooks.objects.filter(issue_by=request.user)
    context = {
        'books': books
    }
    return render(request, 'books/studentsview.html', context)
