from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Shift status'
        verbose_name_plural = 'Shift statuses'
        ordering = ('sort',)


class BreakStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Break status'
        verbose_name_plural = 'Break statuses'
