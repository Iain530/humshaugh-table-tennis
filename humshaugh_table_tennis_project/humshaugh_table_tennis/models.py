from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    #restrictions
    MAX_TITLE_LENGTH=1000
    MAX_CONTENT_LENGTH=20000

    #fields
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    content = models.CharField(max_length=MAX_CONTENT_LENGTH)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'
    
    #functions
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

