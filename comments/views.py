from django.shortcuts import render

# Create your views here.
def get_comment(request):
    return render(request, 'comments/comments.html')