from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from student import Student
from blog.models import Employee
from blog.models import Book, Author
from django import forms

'''
list 3 methods that can render
'''
def index_o(req):
    return HttpResponse('<h1>hello world</h1>')

def index_o2(req):
    t = loader.get_template("index.html")
    c = Context({'title': 'my page1', 'hello': 'hello world1'})
    return HttpResponse(t.render(c))

def index(req):
    # dictionary
    user = {"name": "User", "age": 18}
    # object
    student = Student("Studnet", 30)
    # list
    book = ["java", "c++", "python"]
    
    return render_to_response("index.html", {'title': 'my page', 'hello': 'hello world', "user": user, "student": student, "book": book})


'''
many to many/one to many
'''
def employee(req):
    emps = Employee.objects.all()
    context = {"emps": emps}
    return render_to_response("employee.html", context)

def book(req):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {"books": books, "authors": authors}
    return render_to_response("book.html", context)

'''
form
'''
class UserForm(forms.Form):
    name = forms.CharField()
    
# need to common 'django.middleware.csrf.CsrfViewMiddleware' in settings.py
def register(req):
    if req.method == "POST":
        form = UserForm(req.POST)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponse("ok")
    else:
        form = UserForm()
    context = {"form": form}
    return render_to_response("register.html", context)