from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html', context={})


def about_me(request):
    return render(request, 'aboutme.html', context={})
