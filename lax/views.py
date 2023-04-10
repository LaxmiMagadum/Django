from django.shortcuts import render


posts= [
    {
        'author': 'Laxmi Magadum',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 8, 2023'
    },
    {
        'author': 'Preeti Magadum',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 9, 2023'
    
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request, 'lax/home.html', context)


def about(request):
    return render(request, 'lax/about.html', {'title': 'About'})

