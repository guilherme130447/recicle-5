from django.shortcuts import render


def blog(request):
    return render(request, 'posts/blog.html')


def post1(request):
    return render(request, 'posts/post_1.html')


def post2(request):
    return render(request, 'posts/post_2.html')


def post3(request):
    return render(request, 'posts/post_3.html')
