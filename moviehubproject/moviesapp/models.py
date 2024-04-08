from django.db import models
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True,default=True)
    slug=models.SlugField(max_length=250,unique=True,default=True)
    description=models.TextField(blank=True)
    # image=models.ImageField(upload_to='category',blank=True)

    def get_url(self):
        return reverse('moviesapp:movies_by_category',args=[self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'


    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True, default=True)
    slug = models.SlugField(max_length=250, unique=True,default=True)
    description = models.CharField(max_length=250,blank=True,default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    date=models.DateField()
    actors=models.TextField(max_length=100,null=True,default=True)
    youtube=models.URLField(default=True)
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    # available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('moviesapp:movieCatDetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='movie'
        verbose_name_plural='movies'


    def __str__(self):
        return '{}'.format(self.name)

