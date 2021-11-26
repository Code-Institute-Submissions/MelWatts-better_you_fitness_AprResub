from django.shortcuts import render

# Create your views here.


def get_comments(request):
    return render(request, 'comments/comments.html')