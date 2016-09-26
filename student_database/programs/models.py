from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from students.models import Student


class Program(models.Model):
    students = models.ManyToManyField(Student)
    event_name = models.CharField(max_length=512)

    event_start_date_time = models.DateTimeField(
        help_text=_('Example format: 10/25/2006 14:30')
    )

    event_end_date_time = models.DateTimeField(
        help_text=_('Example format: 10/25/2006 14:30')
    )

    event_address = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text=_("Street address"),
    )

    event_city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("City"),
    )

    event_state = models.CharField(
        max_length=2,
        choices=settings.US_STATES,
        null=True,
        blank=True,
        )

    event_zip = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text=_("Zipcode"),
    )

    event_theme = models.TextField(
        null=True,
        blank=True,
        help_text=_("""Paragraph from staff member about participant activity /
                    involvement""")
    )
