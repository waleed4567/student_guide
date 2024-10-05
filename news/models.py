from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    body = models.TextField(_("Body"),)
    author = models.ForeignKey('auth.User', verbose_name=_("Author"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("Puplish Date"), auto_now=False, auto_now_add=False)
    unit = models.ForeignKey('university_units.Office', verbose_name=_("Unit"), on_delete=models.CASCADE)
    category = models.ForeignKey("news.Category", verbose_name=_("Category"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=256)
    
    def __str__(self):
        return self.name


    