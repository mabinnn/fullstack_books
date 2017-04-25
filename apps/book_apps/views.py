from django.shortcuts import render, HttpResponse, redirect
from .models import Book

def index(request):
    print "I AM YOUR REQUEST FROM THE INDEX def", request
    context = {
        "books" : Book.objects.all()
        #the above line is a query just like this: select * from Book
    }
    print Book.objects.all()
    return render(request, 'book_apps/index.html', context)


def addentry(request):
    # using ORM, code the following:
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    # the above insert into Book table (title, author, catrgory) based on user input by accessing request.POST method.
    print "These are the POSTED information", request
    return redirect('/')

def remove(request, id):
    Book.objects.filter(id=id).delete()
    # make sure to filter and select otherwise, you will delete the entire table.
    # id = id: the second ID is passed through the link.
    return redirect('/')
