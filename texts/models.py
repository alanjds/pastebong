# coding: utf-8
from django.db import models
import datetime

# Create your models here.

FILETYPE_CHOICES = (
    ('python', 'Python'),
    ('json', 'JSON'),
    ('c', 'C'),
)

class Text(models.Model):
    body = models.TextField(u'Corpo do código')
    modified = models.DateTimeField(u'Data de modificação', auto_now=True)
    created = models.DateTimeField(u'Data de criação', auto_now_add=True)
    filetype = models.CharField('Linguagem', max_length=20, choices=FILETYPE_CHOICES, default='python')
    name = models.CharField(u'Título', max_length=50)

    category = models.ForeignKey('Category')

    def __init__(self, *args, **kwargs):
        # Special thing
        result = super(Text, self).__init__(*args, **kwargs)
        # Special thing
        return result

    def __unicode__(self):
        return '%s: %s' % (self.name or '(undefined)', self.filetype)

    @property
    def is_fresh(self):
        today = datetime.date.today()
        if self.created.date() == today:
            return True
        else:
            return False

    @is_fresh.setter
    def is_fresh(self, value):
        import ipdb; ipdb.set_trace()
        if value == True:
            self.created = datetime.datetime.now()
        else:
            self.created = datetime.datetime.now() - datetime.timedelta(1)

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    parent = models.ForeignKey('Category', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Categories'