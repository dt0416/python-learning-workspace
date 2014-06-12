from django.contrib import admin
from blog.models import Employee, User, Book, Author

# Register your models here.
admin.site.register(Employee)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)