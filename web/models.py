from django.db import models
from users.models import Auther

class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        db_table = "web_category"
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["-id"]

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        db_table = "web_tag"
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=225)
    short_discription = models.CharField(max_length=225)
    image = models.ImageField(upload_to="blogs")
    created_on = models.DateTimeField(auto_now=True)
    discription = models.TextField()
    author = models.ForeignKey(Auther, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


    class Meta:
        db_table = "web_blog"
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        ordering = ["-id"]

    def __str__(self):
        return self.title
