from distutils.command.upload import upload
from http.client import PROCESSING
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    PROName = models.CharField(max_length=50, verbose_name=_('Product Name'))
    PROCategory = models.ForeignKey("Category", on_delete= models.CASCADE, blank=True, null=True, verbose_name=_('Product Category'))
    PROBrand = models.ForeignKey('settings.Brand', on_delete= models.CASCADE ,blank=True, null=True,verbose_name=_('Product Brand'))
    PRODiscription = models.TextField(max_length=1000, verbose_name=_("Product Description"))
    PROImg = models.ImageField(upload_to='product/', verbose_name=_("Image"), blank=True, null=True)
    PROPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PROCoast = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PROCreated = models.DateTimeField(verbose_name=_("Created At "))
    
    PROSlug = models.SlugField(blank=True, null=True)
    
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    
    def save(self, *args, **kwargs):
        if not self.PROSlug :
            self.PROSlug = slugify(self.PROName)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.PROName
    
    
class ProductImage(models.Model):
    PROIproduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PROImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))
    
    def __str__(self):
        return str(self.PROIproduct)
    
class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_("Category Name"))
    CATParent = models.ForeignKey("self", limit_choices_to={'CATParent__isnull': True},on_delete=models.CASCADE, blank=True, null=True)
    CATDesceiption = models.TextField(max_length=3000, verbose_name=_("Category Description"))
    CATImage = models.ImageField(upload_to="category/",verbose_name=_('Category Image'))
    
    def __str__(self):
        return str(self.CATName)
    
class ProductAlternative(models.Model):
    PROAProduct= models.ForeignKey('Product',on_delete=models.CASCADE, related_name='main_product',verbose_name='Product')
    PROAlternative = models.ManyToManyField('Product', related_name='alternative_products', verbose_name='Alternative')
    
    class Meta:
        verbose_name = _('Product Alternative')
        verbose_name_plural = _('Product Alternatives')
        
    def __str__(self):
        return str(self.PROAProduct)



class Product_Accessories(models.Model):
    PROACProduct= models.ForeignKey('Product',on_delete=models.CASCADE, related_name='mainAccessories_product',verbose_name='Product')
    PROACcesseies = models.ManyToManyField('Product', related_name='accessoris_products', verbose_name='Accessories')
    
    class Meta:
        verbose_name = _('Product Accessory')
        verbose_name_plural = _('Product Accessories')
        
    def __str__(self):
        return str(self.PROACProduct)





    
    