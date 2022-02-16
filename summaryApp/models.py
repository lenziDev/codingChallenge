from django.db import models
from .summarizers import *
from django.db.models.signals import pre_save
from django.dispatch import receiver
from decouple import config

class Document(models.Model):
    text = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(verbose_name='Created at', db_column='createdAt', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at',db_column='updatedAt', auto_now=True)

    def summarize_sumy_LexRank(self):
        return Sumy(self.text).LexRank()

    def summarize_sumy_Luhn(self):
        return Sumy(self.text).Luhn()
    
    def summarize_sumy_LSA(self):
        return Sumy(self.text).LSA()

    def set_summary(self, method="LSA"):
        print(f"------------ App running using {method}")

        if method == "LSA":
            self.summary = self.normalize_sentences(self.summarize_sumy_LSA())
        elif method == "LexRank":
            self.summary = self.normalize_sentences(self.summarize_sumy_LexRank())
        elif method == "Luhn":
            self.summary = self.normalize_sentences(self.summarize_sumy_Luhn())

        return self

    def normalize_sentences(self, sentences):
        text = ""
        for sentence in sentences:
            if text == "":
                text = f"{sentence}"
            else:
                text += f" {sentence}"
        return text

    class Meta:
        verbose_name_plural = 'Documents'
        verbose_name = 'Document'


@receiver(pre_save, sender=Document)
def set_summary(sender, instance,**kwargs):
    if instance.id == None:
        instance = instance.set_summary(method=str(config("SUMMARIZE_METHOD")))