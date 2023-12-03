from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Model Product contains the detailed product information
    with foreign keys to the related category models
    """

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    sku = models.CharField(
        max_length=254)
    name = models.CharField(
        max_length=254)
    product_description = models.TextField()
    sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True)
    master_category = models.ForeignKey(
        'MasterCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    special_offer = models.ForeignKey(
        'SpecialOffer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    image = models.ImageField(
        blank=True,
        null=True)

    def __str__(self):
        return self.name

class MasterCategory(models.Model):
    """
    Model MasterCategory allows the grouping of products
    for easier searches by main category of item or product
    """
    class Meta:
        verbose_name_plural = 'Master Categories'

    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def master_category_display_name(self):
        return self.display_name

class SpecialOffer(models.Model):
    """
    Model SpecialOffers allows the grouping of products
    for easier searches by adding an extra special offer category
    """
    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def special_offer_display_name(self):
        return self.display_name
