from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Inception',
            'year': 2010
        },
        {
            'id': 3,
            'title': 'Oppenheimer',
            'year': 2023
        },
        {
            'id': 32,
            'title': 'Interstellar',
            'year': 2012
        }
    ]
}

def movies(req):
    return render(req, 'movies/movies.html', data)

def home(req):
    return HttpResponse("<h1>Home page</h1>")