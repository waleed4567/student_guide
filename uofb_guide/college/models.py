from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils.translation import gettext_lazy as _


class College(models.Model):
    name = models.CharField(_("College Name"), max_length=256, unique=True)
    contact = models.CharField(_("College Registeration Office Contact Number"), max_length=16)
    location = models.TextField(_("College Location"))
    description = models.TextField(_("College Description"))

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(_("Year Tag"), max_length=50)
    college = models.ForeignKey("college.College", verbose_name=_("College"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.college} | {self.name}"
  

class Anouncement(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    date = models.DateTimeField(_("Puplish Date"), auto_now=False, auto_now_add=False)
    college = models.ForeignKey('college.College', verbose_name=_("College"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title