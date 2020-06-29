from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    return render(request, 'library/index.html')


def students_list(request):
    user = get_user_model()
    user = user.objects.all().order_by('first_name')
    context = {
        'user_list': user
    }
    return render(request, 'library/studentslist.html', context)
