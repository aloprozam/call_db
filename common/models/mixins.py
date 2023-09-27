from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseDictModelMixin(models.Model):
    code = models.CharField(verbose_name='Code', max_length=16, primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=32,)
    sort = models.PositiveSmallIntegerField(verbose_name='Sorting', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Activity', default=True)

    class Meta:
        ordering = ('sort',)
        abstract = True

    def __str__(self):
        return f'{self.code} ({self.name})'
