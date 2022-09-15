from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Brand(models.Model):
    BRAName = models.CharField(max_length=40, verbose_name=_('Brand Name'))
    BRADesc = models.TextField(max_length=400 , blank= True, null= True)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
    
    def __str__(self):
       return self.BRAName
   
class Variant(models.Model):
    VARName = models.CharField(max_length=40, verbose_name=_('Variant Name'))
    VARDesc = models.TextField(max_length=400 , blank= True, null= True)

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")
    
    def __str__(self):
       return self.VARName
   