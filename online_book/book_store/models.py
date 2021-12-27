from django.db import models


class user_reg(models.Model):
    ''' Store user registration details '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)


class book_details(models.Model):
    ''' Store available book details '''
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_image = models.ImageField()
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title+" - "+self.author



