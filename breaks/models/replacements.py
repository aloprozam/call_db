from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='replacements',
        verbose_name='Employee'
    )
    replacement = models.ForeignKey(
        to='breaks.Replacement', on_delete=models.CASCADE, related_name='employees',
        verbose_name='Shift'
    )
    status = models.ForeignKey(
        to='breaks.ReplacementStatus', on_delete=models.RESTRICT, related_name='replacement_employees',
        verbose_name='Status'
    )

    class Meta:
        verbose_name = 'Shift - Employee'
        verbose_name_plural = 'Shift - Employees'
        ordering = ('status',)

    def __str__(self):
        return f' Shift {self.replacement} for {self.employee} '


class Replacement(models.Model):
    group = models.ForeignKey(
        to='breaks.Group', on_delete=models.CASCADE, related_name='replacements',
        verbose_name='Group',
    )
    date = models.DateField('Shift Date')
    break_start = models.TimeField('Break Start')
    break_end = models.TimeField('Break End')
    break_max_duration = models.PositiveSmallIntegerField('Max Break Duration')

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        ordering = ('-date',)

    def __str__(self):
        return f' Shift №{self.pk} for {self.group} '
