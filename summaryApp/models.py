from django.db import models

# Create your models here.

class Document(models.Model):
    text = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(verbose_name='Created at', db_column='createdAt', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at',db_column='updatedAt', auto_now=True)

    class Meta:
        verbose_name_plural = 'Documents'
        verbose_name = 'Document'