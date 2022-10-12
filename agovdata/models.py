from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.
class People(models.Model):
    SEX_CHOICES = (
        ('1', 'หญิง'),
        ('2', 'ชาย'),
    )
    NID = models.CharField(_("Nid"),max_length=15, blank=False, null=False)
    TITLE = models.CharField(max_length=50, blank=False, null=False)
    F_NAME = models.CharField(max_length=150, blank=False, null=False)
    L_NAME = models.CharField(max_length=150, blank=False, null=False)
    BIRTH_DATE = models.CharField(max_length=36, blank=True, null=True)
    HOUSE_CODE = models.CharField(max_length=11, blank=True, null=True)
    SEX_CARD = models.CharField(max_length = 1,choices=SEX_CHOICES)
    BODY_CODE = models.CharField(max_length=1, blank=False, null=False)
    DISABLED_CODE = models.CharField(max_length=1, blank=True, null=True)
    KEEPER_CODE = models.CharField(max_length=1, blank=True, null=True)
    CURATOR_CODE = models.CharField(max_length=1, blank=True, null=True)
    PHONE_MOBILE = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering =('-NID','TITLE')
        verbose_name = _("People")
        verbose_name_plural = _("Peoples")

    def __str__(self):
        return self.NID 

class Name(models.Model):
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 

