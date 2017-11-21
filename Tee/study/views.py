from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse('HELLO python')


def show(request):
    data = {}
    data['name'] = 'Test'
    data['age'] = 22
    return render(request, 'study/show.html', data)

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)

    c = int(a) + int(b)

    data = {'sum': c}
    return render(request, 'study/add.html', data)

def sum(request, a, b):
    c = int(a) + int(b)
    data = {'sum': c}

    return render(request, 'study/add.html', data)

def tpl(request):
    data = {}

    data['tpl_str'] = u'my python test'
    data['tpl_tuple'] = ('a', 'b', 'c')
    data['tpl_list'] = ['java', 'php', 'python', 'scala', 'lua']
    data['tpl_dict'] = {'name':'test', 'age':22, 'email':'123456@126.com'}

    return render(request, 'study/tpl.html', data)

def page(request, page):
    data = {'page': page}
    return render(request, 'study/page.html', data)







