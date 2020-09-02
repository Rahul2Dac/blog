from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Rahul',
        'title'  : 'Blog Post 1',
        'content': 'First post content',
        'date posted': 'August 27, 2020'

    },
    {
        'author' : 'Akkz',
        'title'  : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2020'

    }

]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)


def about(request):
     return render(request,'blog/about.html')