from django.shortcuts import HttpResponse, render

def index(request):
    return HttpResponse('Главная страница сайта.')


def group_posts(request, slug):
    return HttpResponse('На этой странице сайта, вы можете видеть посты про что-то. Или пока не можете.')
