from django.contrib.auth import get_user_model
from django.db import models
from breaks.constants import BREAK_CREATED_STATUS, BREAK_CREATED_DEFAULT
from breaks.models.dicts import BreakStatus

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.replacement', models.RESTRICT, 'breaks',
        verbose_name='Shift',
    )
    employee = models.ForeignKey(

        User, models.CASCADE, 'breaks',
        verbose_name='Employee'
    )
    break_start = models.TimeField('Break Start', null=True, blank=True)
    break_end = models.TimeField('Break End', null=True, blank=True)
    # duration = models.PositiveSmallIntegerField('Break Timing', null=True, blank=True)
    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT, 'breaks', verbose_name='Status',
        blank=True
    )

    class Meta:
        verbose_name = 'Break Time'
        verbose_name_plural = 'Break Times'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f'Break user{self.employee} ({self.pk})'

    def save(self, *args, **kwargs):
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_CREATED_STATUS,
                defaults=BREAK_CREATED_DEFAULT
            )

            self.status = status
        return super(Break, self).save(*args, **kwargs)
