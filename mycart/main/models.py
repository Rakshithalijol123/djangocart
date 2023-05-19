from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    catagery = (
        ('fashion','fashion'),
        ('electronics', 'electronics'),
        ('accessories', 'accessories')
    )
    sub_cat = (
        (
            catagery[0][0],(
                ('kids','kids'),
                ('womens','womens'),
                ('mens','mens'),
            )
        ),
            (
            catagery[1][0], (
            ('mobile', 'mobile'),
            ('laptop', 'laptop'),
            ('ipad', 'ipad'),
            ('power bank', 'power bank'),
        )
        ),
        (
            catagery[2][0], (
                ('earring', 'earring'),
                ('earphone', 'earphone'),
                ('watch', 'watch'),
                ('sunglass', 'sunglass'),
            )
        )
    )
    p_name = models.CharField(max_length=100)
    p_price = models.FloatField(default=0.0)
    p_disc = models.TextField()
    p_img = models.ImageField(upload_to='pics')
    p_cat = models.CharField(max_length=100,choices=catagery)
    p_sub_cat = models.CharField(max_length=100, choices=sub_cat,default='pant')
    p_specification = models.CharField(max_length=100,default="pant")

    def __str__(self):
        return self.p_name

class Search_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    data = models.TextField()
    searched_on = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.user}"

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart_on = models.DateField(default=timezone.now())

    def __str__(self):
        return str(self.user)
