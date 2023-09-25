from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField(verbose_name='Code', max_length=16, primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=32,)
    sort = models.PositiveSmallIntegerField(verbose_name='Sorting', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Activity', default=True)

    class Meta:
        verbose_name = 'Shift status'
        verbose_name_plural = 'Shift statuses'
        ordering = ('sort',)

    def __str__(self):
        return f'{self.code} for {self.name} '


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
