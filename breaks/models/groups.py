from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    organisation = models.ForeignKey(
        to='breaks.Organisation', on_delete=models.CASCADE, related_name='groups',
        verbose_name='Organisation'
    )
    name = models.CharField('Name', max_length=255)
    manager = models.ForeignKey(
        to=User, on_delete=models.RESTRICT, related_name='group_managers',
        verbose_name='Manager'
    )
    employees = models.ManyToManyField(
        to=User, related_name='group_employees',
        verbose_name='User',
        blank=True
    )
    min_active = models.PositiveSmallIntegerField(
        'Minimal active workers',
        null=True,
        blank=True
    )
    break_start = models.TimeField('Break Start', blank=True, null=True)
    break_end = models.TimeField('Break End', blank=True, null=True)
    break_max_duration = models.PositiveSmallIntegerField('Break Max Duration', blank=True, null=True)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'
