from django.db import models
from django.utils.translation import ugettext as _

from django_countries.fields import CountryField
from django.conf import settings


GENDER_CHOICES = (('Male', 'Male'),
                  ('Female', 'Female'),
                  ('Other', 'Other'),
                  ('Prefer not to say', 'Prefer not to say'))


class Student(models.Model):
    first_name = models.CharField(max_length=512,
                                  null=False,
                                  db_index=True,
                                  help_text=_("First Name"))

    last_name = models.CharField(max_length=512,
                                 null=True,
                                 db_index=True,
                                 help_text=_("Last Name"))

    address = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text=_("Street address"),
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("City"),
    )
    state = models.CharField(
        max_length=2,
        choices=settings.US_STATES,
        null=True,
        blank=True,
        )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=30,
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        )

    zip = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text=_("Zipcode"),
    )

    country = CountryField(null=True)

    def __unicode__(self):
        return u'{0}-{1}'.format(self.id, self.first_name)

    class Meta:
        verbose_name = _("Student Base")


class StaffContact(models.Model):
    student = models.ForeignKey(Student)
    note = models.TextField()
    conversation_date_time = models.DateTimeField(
        help_text=_('Example format: 10/25/2006 14:30')
    )
