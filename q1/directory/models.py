from django.db import models
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=200)
    num_visits = models.IntegerField(default=0)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=200)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# Form for Category model
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'num_visits', 'num_likes']


# Form for Page model
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ['category']
