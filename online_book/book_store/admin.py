from django.contrib import admin
from .models import book_details, user_reg

# Register your models here.
admin.site.register(book_details)
admin.site.register(user_reg)
