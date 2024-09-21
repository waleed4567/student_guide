from django.db import models
from django.utils.translation import gettext_lazy as _

class Chapter(models.Model):
    number = models.IntegerField(_('Number'))
    title = models.CharField(_('Title'), max_length=256)
    
    def __str__(self):
        return self.title
    # New Line 

class GuideTopic(models.Model):
    chapter = models.ForeignKey(to=Chapter, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=128)
    ar_title = models.CharField(_('Arabic Title'), max_length=128)
    content = models.TextField(_('Content'))
    ar_content = models.TextField(_('Arabic Content'))
    image = models.ImageField(_("Guide Entry Image"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    # added_by_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # updated_by_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    # unit = models.ForeignKey('university_units.Office', verbose_name=_("Unit"), on_delete=models.CASCADE)
    created = models.DateTimeField(_('Created At'), auto_created=True)
    updated = models.DateTimeField(_('Updated At'), auto_created=True, auto_now=True)

    def __str__(self):
        return self.title + "|" + self.ar_title
    # New Line 

