from django.db import models
from django.utils import formats
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(_('title'), max_length=80)
    date = models.DateField(_('date'))
    description = models.FileField(_('description'), blank=True)

    def __str__(self):
        return _('{title} at {date}').format(
            title=self.title, date=formats.date_format(self.date, "SHORT_DATE_FORMAT"))

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
