from django.db import models
from django.utils.translation import ugettext as _


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
    # state = models.CharField(
    #     FIPSState,
    #     null=True,
    #     blank=True,
    #     db_column='state',
    #     on_delete=models.PROTECT,
    #     related_name='location_state',
    #     help_text=_("State"),
    # )

    zip = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text=_("Zipcode"),
    )

    region = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Region"),
    )
    country = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Country"),
    )

    def __unicode__(self):
        return u'{0}-{1}'.format(self.unique_id, self.first_name)

    # class Meta:
    #     app_label = 'student_database'
    #     db_table = 'student_base_info'
    #     verbose_name = _("Student Base")
