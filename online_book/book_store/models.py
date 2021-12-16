from django.db import models

# Create your models here.
class user_reg(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)


class book_details(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_image = models.ImageField()
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title+" - "+self.author

