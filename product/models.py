from __future__ import unicode_literals
from django.db import models
from photologue.models import Gallery



class Craft(models.Model):
    craft_name = models.CharField(max_length = 255)
    craft_slug = models.SlugField()
    craft_description = models.TextField(null = True)
    gallery = models.OneToOneField(Gallery,related_name = 'craft_gallery', null = True, blank = True)

    def __unicode__(self):
		return self.craft_name

    class Meta:
        verbose_name_plural = "Crafts"



class Category(models.Model):
    category_name = models.CharField(max_length = 255)
    category_description = models.TextField()
    category_slug = models.SlugField()

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"




class Product(models.Model):
    product_name = models.CharField(max_length = 255)
    product_slug = models.SlugField()
    product_description = models.TextField()
    category = models.ForeignKey(Category, null = True, blank = True)
    craft = models.ForeignKey(Craft, null = True, blank = True)
    price = models.IntegerField()
    gallery = models.OneToOneField(Gallery,related_name = 'product_gallery', null = True, blank = True)

    def __unicode__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Products"
