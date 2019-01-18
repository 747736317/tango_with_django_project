from django.shortcuts import render
from rango.models import Category

def index(request):
    # retrieve top 5 likes categories
    # '-likes' -> descending order
    # place list in the dictionary
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': "here is the about message"}
    return render(request, 'rango/about.html', context=context_dict)