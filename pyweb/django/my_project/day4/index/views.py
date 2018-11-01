from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def parent_views(request):
    return render(request, 'parent.html')

def child_views(request):
    return render(request, 'child.html')

def add_author_views(request):
    obj = Author(name='jianailiang',age=35,email='jia@green.com')
    obj.save()
    # Author.objects.create(name='baoqiang', age=33, email='baoqiang@163.com')
    return HttpResponse('Add OK')

def add_book_views(request):
    Book.objects.create(title='红楼梦',publication_date='1995-12-12')

    obj = Book(title='西游记',publication_date='1982-10-12')
    obj.save()

    dic = {
        'title' : '三国演义',
        'publication_date': '1990-3-5'
    }
    book = Book(**dic)
    book.save()

    return HttpResponse('Add Book OK')

def add_publisher_views(request):
    Publisher.objects.create(name='中国人民出版社',address='五道口',\
                             city='北京',country='北京',website='http://www.renmin.com')

    obj = Publisher(name='中国动画出版社',address='潘家园',\
                    city='北京',country='中国',website='http://www.donghuapian.com')
    obj.save()

    dic = {
        'name': '中国文化出版社',
        'address': '潘家园',
        'city': '北京',
        'country':'中国',
        'website':'http://wenhua.com'
    }
    publisher = Publisher(**dic)
    publisher.save()

    return HttpResponse("Add Publisher OK")

def get_author_views(request):
    # authors = Author.objects.all()
    # authors =Author.objects.values("name", "age", "id")
    # authors = Author.objects.all().values("name","age")
    # auth = Author.objects.get(id=1)
    # authors = Author.objects.exclude(age=35)
    authors = Author.objects.all().order_by('-age')

    return render(request, 'show_authors.html', locals())

def all_authors_views(request):
    author = Author.objects.all()
    return render(request, 'all_authors.html',locals())

def oto_views(request):
    w = Wife.objects.get(id=1)
    a = w.author

    au = Author.objects.get(id=2)
    wi = au.wife
    return render(request, 'oto.html', locals())

def otm_views(request):
    book = Book.objects.get(id=1)
    publisher = book.publisher

    pub = Publisher.objects.get(id=1)
    books = pub.book_set.all()

    return render(request,'otm.html',locals())

def mtm_views(request):
    author = Author.objects.get(id=2)
    pubLish = author.publisher.all()

    pub = Publisher.objects.get(id=3)
    authors = pub.author_set.all()

    return render(request,'mtm.html',locals())

def book_author_views(request):
    book = Book.objects.get(id=3)
    auList = book.author.all()

    au = Author.objects.get(id=3)
    bookList = au.book_set.all()
    return render(request,'12.html',locals())